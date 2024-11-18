import pygame
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic, Water, WildFlower, Tree, Interaction, Particle
from pytmx.util_pygame import load_pygame
from support import *
from transition import Transition
from soil import SoilLayer
from sky import Rain, Sky
from random import randint
from menu import Menu1
from menu2 import Menu2
from menu3 import Menu3
from menu4 import Menu4
from menu5 import Menu5
from menu6 import Menu6
from menu7 import Menu7

class Level:
	def __init__(self):

		# Inicializar shop_active e shop2_active como False
		self.shop_active = False
		self.shop2_active = False
		self.shop3_active = False
		self.shop4_active = False
		self.shop5_active = False
		self.shop6_active = False
		self.shop7_active = False

		# get the display surface
		self.display_surface = pygame.display.get_surface()
		
		# sprite groups
		self.all_sprites = CameraGroup()
		self.collision_sprites = pygame.sprite.Group()
		self.tree_sprites = pygame.sprite.Group()
		self.interaction_sprites = pygame.sprite.Group()

		self.soil_layer = SoilLayer(self.all_sprites, self.collision_sprites)
		self.setup()
		self.overlay = Overlay(self.player)
		self.transition = Transition(self.reset, self.player)

		# sky
		self.rain = Rain(self.all_sprites)
		self.raining = randint(0,10) > 7
		self.soil_layer.raining = self.raining
		self.sky = Sky()

		# Menus
		self.menu = Menu1(self.player, self.toggle_shop, correct_indices=[0, 3, 2]) 
		self.menu2 = Menu2(self.player, self.toggle_shop2, correct_indices=[0, 3, 2])
		self.menu3 = Menu3(self.player, self.toggle_shop3, correct_indices=[3, 2, 0, 0, 1])
		self.menu4 = Menu4(self.player, self.toggle_shop4, correct_indices=[1, 2, 1, 0, 0])
		self.menu5 = Menu5(self.player, self.toggle_shop5, correct_indices=[1, 0, 1, 1, 0, 2])
		self.menu6 = Menu6(self.player, self.toggle_shop6, correct_indices=[2, 2, 1, 1, 1, 1])
		self.menu7 = Menu7(self.player, self.toggle_shop7, correct_indices=[1, 1, 1, 0, 1, 1])

		# music
		self.success = pygame.mixer.Sound('audio/success.wav')
		self.success.set_volume(0.1)
		self.music = pygame.mixer.Sound('audio/music.mp3')
		self.music.set_volume(0.1)
		self.music.play(loops=-1)

	def setup(self):
		tmx_data = load_pygame('data/map.tmx')

		# house 
		for layer in ['HouseFloor', 'HouseFurnitureBottom']:
			for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
				Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, LAYERS['house bottom'])

		for layer in ['HouseWalls', 'HouseFurnitureTop']:
			for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
				Generic((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

		# Fence
		for x, y, surf in tmx_data.get_layer_by_name('Fence').tiles():
			Generic((x * TILE_SIZE, y * TILE_SIZE), surf, [self.all_sprites, self.collision_sprites])

		# water 
		water_frames = import_folder('graphics/water')
		for x, y, surf in tmx_data.get_layer_by_name('Water').tiles():
			Water((x * TILE_SIZE, y * TILE_SIZE), water_frames, self.all_sprites)

		# trees 
		for obj in tmx_data.get_layer_by_name('Trees'):
			Tree(
				pos=(obj.x, obj.y), 
				surf=obj.image, 
				groups=[self.all_sprites, self.collision_sprites, self.tree_sprites], 
				name=obj.name,
				player_add=self.player_add)

		# wildflowers 
		for obj in tmx_data.get_layer_by_name('Decoration'):
			WildFlower((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

		# collision tiles
		for x, y, surf in tmx_data.get_layer_by_name('Collision').tiles():
			Generic((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites)

		# Player 
		for obj in tmx_data.get_layer_by_name('Player'):
			if obj.name == 'Start':
				self.player = Player(
					pos=(obj.x, obj.y), 
					group=self.all_sprites, 
					collision_sprites=self.collision_sprites,
					tree_sprites=self.tree_sprites,
					interaction=self.interaction_sprites,
					soil_layer=self.soil_layer,
					toggle_shop=self.toggle_shop,
					toggle_shop2=self.toggle_shop2,
					toggle_shop3=self.toggle_shop3,
					toggle_shop4=self.toggle_shop4,
					toggle_shop5=self.toggle_shop5,
					toggle_shop6=self.toggle_shop6,
					toggle_shop7=self.toggle_shop7
				)
			
			if obj.name == 'Bed':
				Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'gays':  # Placeholder para interação que não afeta ciclo de dia/noite
				Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)

			if obj.name == 'Trader':
				Interaction((obj.x, obj.y), (obj.width, obj.height), self.interaction_sprites, obj.name)

		Generic(
			pos=(0, 0),
			surf=pygame.image.load('graphics/world/ground.png').convert_alpha(),
			groups=self.all_sprites,
			z=LAYERS['ground'])

	def player_add(self, item):
		self.player.item_inventory[item] += 1
		self.success.play()

	def toggle_shop(self):
		# Alterna o estado de shop_active
		self.shop_active = not self.shop_active

	def toggle_shop2(self):
		# Alterna o estado de shop2_active
		self.shop2_active = not self.shop2_active
	
	def toggle_shop3(self):
		# Alterna o estado de shop3_active
		self.shop3_active = not self.shop3_active

	def toggle_shop4(self):
		# Alterna o estado de shop4_active
		self.shop4_active = not self.shop4_active

	def toggle_shop5(self):
		# Alterna o estado de shop5_active
		self.shop5_active = not self.shop5_active

	def toggle_shop6(self):
		# Alterna o estado de shop2_active
		self.shop6_active = not self.shop6_active

	def toggle_shop7(self):
		# Alterna o estado de shop7_active
		self.shop7_active = not self.shop7_active

	def reset(self):
		# Atualização de plantas e solo para novo ciclo
		self.soil_layer.update_plants()
		self.soil_layer.remove_water()
		self.raining = randint(0, 10) > 7
		self.soil_layer.raining = self.raining
		if self.raining:
			self.soil_layer.water_all()
		self.sky.start_color = [255, 255, 255]

	def plant_collision(self):
		if self.soil_layer.plant_sprites:
			for plant in self.soil_layer.plant_sprites.sprites():
				if plant.harvestable and plant.rect.colliderect(self.player.hitbox):
					self.player_add(plant.plant_type)
					plant.kill()
					Particle(plant.rect.topleft, plant.image, self.all_sprites, z=LAYERS['main'])
					self.soil_layer.grid[plant.rect.centery // TILE_SIZE][plant.rect.centerx // TILE_SIZE].remove('P')

	def run(self, dt):
		# drawing logic
		self.display_surface.fill('black')
		self.all_sprites.custom_draw(self.player)

		# updates
		if self.shop_active:
			self.menu.update()  # Mostra o menu1
		elif self.shop2_active:
			self.menu2.update()  # Mostra o menu2
		elif self.shop3_active:
			self.menu3.update()  # Mostra o menu3
		elif self.shop4_active:
			self.menu4.update()  # Mostra o menu4
		elif self.shop5_active:
			self.menu5.update()  # Mostra o menu5
		elif self.shop6_active:
			self.menu6.update()  # Mostra o menu6
		elif self.shop7_active:
			self.menu7.update()  # Mostra o menu7
		else:
			# Atualizações normais quando nenhum menu está ativo
			self.all_sprites.update(dt)
			self.plant_collision()

		# weather
		self.overlay.display()
		if self.raining and not (self.shop_active or self.shop2_active or self.shop3_active or self.shop4_active or self.shop5_active or self.shop6_active or self.shop7_active):
			self.rain.update()
		self.sky.display(dt)

		# transition overlay
		if self.player.sleep:
			self.transition.play()

class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.math.Vector2()

	def custom_draw(self, player):
		self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
		self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

		for layer in LAYERS.values():
			for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
				if sprite.z == layer:
					offset_rect = sprite.rect.copy()
					offset_rect.center -= self.offset
					self.display_surface.blit(sprite.image, offset_rect)
