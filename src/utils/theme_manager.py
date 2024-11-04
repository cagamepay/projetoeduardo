# Implementação do gerenciador de temas (exemplo básico)
class ThemeManager:
    def __init__(self):
        self.theme_config = self.load_theme_config()

    def load_theme_config(self):
        with open("assets/themes/theme_config.json", "r") as f:
            return json.load(f)

    def get_background_color(self):
        return self.theme_config["background_color"]

    def get_button_color(self):
        return self.theme_config["button_color"]

    def get_text_color(self):
        return self.theme_config["text_color"]

    def get_footer_color(self):
        return self.theme_config["footer_color"]