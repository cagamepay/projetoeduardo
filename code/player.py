import pygame
from settings import *
from support import *
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites, tree_sprites, interaction, soil_layer, toggle_shop, toggle_shop2):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # General setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # Movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        # Collision
        self.hitbox = self.rect.copy().inflate((-126, -70))
        self.collision_sprites = collision_sprites

        # Timers (removido 'tool use' e 'tool switch')
        self.timers = {
            'seed use': Timer(350, self.use_seed),
            'seed switch': Timer(200),
        }

        # Seeds
        self.seeds = ['tomato']
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

        # Inventory
        self.item_inventory = {}
        self.seed_inventory = {'tomato': 3}
        self.money = 200

        # Interaction
        self.tree_sprites = tree_sprites
        self.interaction = interaction
        self.sleep = False
        self.soil_layer = soil_layer
        self.toggle_shop = toggle_shop
        self.toggle_shop2 = toggle_shop2

        # Sound
        self.watering = pygame.mixer.Sound('audio/water.mp3')
        self.watering.set_volume(0.2)

    def use_seed(self):
        if self.seed_inventory[self.selected_seed] > 0:
            self.soil_layer.plant_seed(self.target_pos, self.selected_seed)
            self.seed_inventory[self.selected_seed] -= 1

    def import_assets(self):
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': []
        }
        for animation in self.animations.keys():
            full_path = 'graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.sleep:
            # Direction input
            self.direction.y = -1 if keys[pygame.K_UP] else (1 if keys[pygame.K_DOWN] else 0)
            self.direction.x = 1 if keys[pygame.K_RIGHT] else (-1 if keys[pygame.K_LEFT] else 0)

            if self.direction.y != 0 or self.direction.x != 0:
                self.status = 'up' if self.direction.y == -1 else ('down' if self.direction.y == 1 else ('right' if self.direction.x == 1 else 'left'))

            # Seed usage
            if keys[pygame.K_LCTRL]:
                self.timers['seed use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
            if keys[pygame.K_e] and not self.timers['seed switch'].active:
                self.seed_index = (self.seed_index + 1) % len(self.seeds)
                self.selected_seed = self.seeds[self.seed_index]
                self.timers['seed switch'].activate()

            # Interaction with NPCs
            if keys[pygame.K_RETURN]:
                collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interaction, False)
                if collided_interaction_sprite:
                    npc_name = collided_interaction_sprite[0].name
                    if npc_name == 'Trader':
                        self.toggle_shop()
                    elif npc_name == 'gays':
                        self.toggle_shop2()
                    else:
                        self.status = 'left_idle'
                        self.sleep = True

    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:  # moving right
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:  # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx

                    if direction == 'vertical':
                        if self.direction.y > 0:  # moving down
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:  # moving up
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.hitbox.centerx, self.rect.centerx = round(self.pos.x), self.hitbox.centerx
        self.collision('horizontal')
        self.hitbox.centery, self.rect.centery = round(self.pos.y), self.hitbox.centery
        self.collision('vertical')

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
    #    self.get_target_pos()
        self.move(dt)
        self.animate(dt)
