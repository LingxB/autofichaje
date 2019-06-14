# AutoFichaje

This project only aims to automate the process of marking work hours.

## Getting Started

1. Clone or download repository.

        git clone https://github.com/LingxB/autofichaje.git
    
2. Install related packages from `requirements.txt`.

        pip install -r requirements.txt
        
3. Create a `.env` file specifying your credentials at project root directory. File should contain following
environment variables:
    
        USER_NIE = <your_id>
        USER_PASSWORD = <password>
        A3HRGO_URL = https://bcrabogados.a3hrgo.com/
        DRIVER_PATH = drivers/chromedriver.exe
        
4. Run following command from `cmd` at project root directory.

        script a3hrgo
        
        # Hours to be marked can be passed as optional argument, default 8 hours.
        script a3hrgo -h 4
