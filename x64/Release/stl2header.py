def file_to_cpp_header(input_filename, output_filename, array_name):
    try:
        # Read the binary content of the input file
        with open(input_filename, 'rb') as file:
            content = file.read()

        # Convert the binary content to a C++ unsigned char array
        array_content = ', '.join(f'0x{byte:02x}' for byte in content)

        # Prepare the header content
        header_content = f"""#pragma once

// Data for {input_filename}, automatically generated
const unsigned char {array_name}[] = {{
    {array_content}
}};
const size_t {array_name}Size = sizeof({array_name}) / sizeof({array_name}[0]);
"""

        # Write the header file
        with open(output_filename, 'w') as file:
            file.write(header_content)
        
        print(f"Successfully converted {input_filename} to {output_filename}")

    except IOError as e:
        print(f"Error processing file: {e}")

# Example usage
file_to_cpp_header('C:/Users/kline/Desktop/DEV/_done______________________/PTS2STL/x64/Release/sphere.stl', 'C:/Users/kline/Desktop/DEV/_done______________________/PTS2STL/x64/Release/sphere_stl.h', 'sphereStlData')
