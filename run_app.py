import sys
import os
import logging

def main():
    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app_debug.log'),
            logging.StreamHandler()
        ]
    )
    
    logging.info("Starting application...")
    
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"Base directory: {base_dir}")
    
    # Add both the base directory and Windows_and_Linux directory to the Python path
    sys.path.insert(0, base_dir)
    sys.path.insert(0, os.path.join(base_dir, 'Windows_and_Linux'))
    logging.info(f"Python path: {sys.path}")
    
    # Set the working directory to the base directory
    os.chdir(base_dir)
    logging.info(f"Current working directory: {os.getcwd()}")
    
    try:
        from Windows_and_Linux.WritingToolApp import WritingToolApp
        logging.info("Successfully imported WritingToolApp")
        print("Starting Writing Tools...")
        app = WritingToolApp(sys.argv)
        
        # Create an event loop to keep the application running
        from PySide6.QtCore import QEventLoop
        loop = QEventLoop()
        app.aboutToQuit.connect(loop.quit)
        
        logging.info("Application initialized successfully")
        app.exec()
    except Exception as e:
        logging.error(f"Error: {e}")
        import traceback
        logging.error(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main() 