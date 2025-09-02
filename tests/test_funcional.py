@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(['streamlit', 'run', 'src/app.py'])
    options = Options()
    options.headless = True # Executar em modo headless
    driver = webdriver.Firefox(options=options)
    # Iniciar  o WebDriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title_is(driver):
    # Verifica se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o título da página é
    sleep(2)
    # Capturar o título da página
    