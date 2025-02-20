# src/frontend/whatsapp_actions.py

class WhatsAppActions:
    def __init__(self, browser):
        self.browser = browser

    def login(self):
        pass

    def list_conversations(self):
        script = """
        // Ocultar a mensagem de atualização do navegador
        var updateBanner = document.querySelector("div[role='alert']");
        if (updateBanner) {
            updateBanner.style.display = 'none';
        }

        var conversations = [];
        var chatElements = document.querySelectorAll("div[role='row']");
        chatElements.forEach(chat => {
            var name = chat.querySelector("span[title]").getAttribute("title");
            conversations.push(name);
        });
        conversations;
        """
        self.browser.page().runJavaScript(script, self.handle_conversations)

    def handle_conversations(self, conversations):
        print("Conversas:", conversations)  # Aqui você pode armazenar ou exibir as conversas
