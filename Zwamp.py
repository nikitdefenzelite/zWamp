import re
import os


def print_watermark():
    watermark = """
                                                                                          
                                                                                  
                                                                                  
888888888     8b      db      d8  ,adPPYYba,  88,dPYba,,adPYba,   8b,dPPYba,      
     a8P"     `8b    d88b    d8'  ""     `Y8  88P'   "88"    "8a  88P'    "8a     
  ,d8P'        `8b  d8'`8b  d8'   ,adPPPPP88  88      88      88  88       d8     
,d8"            `8bd8'  `8bd8'    88,    ,88  88      88      88  88b,   ,a8"     
888888888         YP      YP      `"8bbdP"Y8  88      88      88  88`YbbdP"'      
                                                                  88              
                                                                  88              
 v1.0 Beta
                                        
          
    Crafted by Defenzelite Private Limited. Unauthorized distribution and usage are strictly prohibited, subject to penalties.
    """
    print(watermark)

def update_php_config(file_path, config_changes):
    with open(file_path, 'r') as file:
        php_config = file.read()

    for config_key, config_value in config_changes.items():
        pattern = re.compile(rf'{config_key}\s*=\s*(.*)', re.IGNORECASE)
        php_config = re.sub(pattern, f'{config_key} = {config_value}', php_config)

    with open(file_path, 'w') as file:
        file.write(php_config)

def update_curl_cainfo(path_to_ini_file, new_path_to_cacert):
    try:
        with open(path_to_ini_file, 'r') as file:
            lines = file.readlines()

        with open(path_to_ini_file, 'w') as file:
            inside_curl_section = False

            for line in lines:
                if line.startswith("[curl]"):
                    inside_curl_section = True
                elif inside_curl_section and line.startswith(";curl.cainfo"):
                    line = f'curl.cainfo = "{new_path_to_cacert}"\n'
                    inside_curl_section = False

                file.write(line)

        print("php.ini updated successfully.")
    except Exception as e:
        print(f"Error updating php.ini: {e}")

def uncomment_php_extensions(php_ini_path):
    # Read the contents of the php.ini file
    with open(php_ini_path, 'r') as file:
        php_ini_content = file.read()

    # Uncomment the specified extension lines
    extensions_to_uncomment = ['extension=ftp', 'extension=odbc', 'extension=json', 'extension=bz2']
    for extension in extensions_to_uncomment:
        php_ini_content = php_ini_content.replace(f';{extension}', extension)

    # Write the modified content back to the php.ini file
    with open(php_ini_path, 'w') as file:
        file.write(php_ini_content)

    print("Done! Uncommented specified extensions in php.ini.")

def main():
    print_watermark()  # Print the watermark when the script starts

    php_ini_path = r'D:\wamp64\bin\php\php8.2.13\php.ini'  # Change this to the actual path of your php.ini file

    while True:
        print("\nChoose an option:")
        print("1. Update PHP Configuration")
        print("2. Update curl.cainfo in php.ini")
        print("3. Uncomment specified extensions in php.ini")
        print("4. Exit")

        choice = input("Enter the number of the option: ")

        if choice == '1':
            # Configuration changes
            config_changes = {
                'memory_limit': '512M',
                'post_max_size': '100M',
                'upload_max_filesize': '20M',
                'max_execution_time': '100',
                'max_input_time': '120',
                'max_input_vars': '5000',
                'max_file_uploads': '20',
                'date.timezone': 'UTC',
            }

            update_php_config(php_ini_path, config_changes)
            print(f'PHP Configuration updated in {php_ini_path}')

        elif choice == '2':
            # Update curl.cainfo configuration in php.ini
            new_cacert_path = r'D:\wamp64\bin\cacert.pem'  # Change this to the actual path of your cacert.pem file
            update_curl_cainfo(php_ini_path, new_cacert_path)

        elif choice == '3':
            # Uncomment specified extensions in php.ini
            uncomment_php_extensions(php_ini_path)

        elif choice == '4':
            print("Exiting the script.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
        

if __name__ == "__main__":
    main()
