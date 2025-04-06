import sys
import os

# Add the Windows_and_Linux directory to Python path
windows_linux_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Windows_and_Linux')
sys.path.append(windows_linux_path)

try:
    from WritingToolApp import WritingToolApp
    print("Successfully imported WritingToolApp")
    
    # Try to create an instance
    app = WritingToolApp(sys.argv)
    print("Successfully created WritingToolApp instance")
    
except Exception as e:
    print("Error:", e)
    import traceback
    traceback.print_exc() 