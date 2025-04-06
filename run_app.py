import sys
import os

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add both the base directory and Windows_and_Linux directory to the Python path
    sys.path.insert(0, base_dir)
    sys.path.insert(0, os.path.join(base_dir, 'Windows_and_Linux'))
    
    # Set the working directory to the base directory
    os.chdir(base_dir)
    
    try:
        from Windows_and_Linux.WritingToolApp import WritingToolApp
        print("Starting Writing Tools...")
        app = WritingToolApp(sys.argv)
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 