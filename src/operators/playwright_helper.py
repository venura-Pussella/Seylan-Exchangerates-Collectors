import subprocess

def install_playwright_browser_binaries():
    try:
        # Install Playwright via pip (it will be installed via requirements.txt, but this is a failsafe)
        subprocess.run(["pip", "install", "playwright", "--no-cache-dir"], check=True)

        print("Playwright installed successfully.")
        
        # Install the Playwright browser binaries
        subprocess.run(["python", "-m", "playwright", "install"], check=True)

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"An error occurred while installing Playwright: {e}")
