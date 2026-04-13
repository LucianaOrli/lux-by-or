from pages.login_page import LoginPage
import os

def test_login_com_usuario_valido(page):
    login_page = LoginPage(page)
    
    # Ação
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Validação (Assertion) - Nível Sênior
    # Verificamos se a URL mudou para a página de inventário
    assert "inventory.html" in page.url
    print("\n[SUCESSO] Login realizado com Page Objects!")

def test_login_com_usuario_invalido(page):
    login_page = LoginPage(page)
    
    # Ação
    login_page.navigate()
    login_page.login("usuario_errado", "senha_errada")
    
    # Validação da mensagem de erro
    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in login_page.error_message.inner_text()
    print("\n[SUCESSO] Validação de erro de login funcionando!")
