import os

def test_deve_abrir_o_site_com_sucesso(page):
    url = os.getenv("BASE_URL")
    page.goto(url)
    
    # Valida se o título da página é o esperado
    assert page.title() == "Swag Labs"
    print("\n[SUCESSO] O Playwright abriu o site corretamente!")
