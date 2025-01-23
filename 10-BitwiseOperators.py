# Bitwise Operators are & , | , ^
# Bitwise operators are commonly used in real-life scenarios where direct manipulation of individual bits is required. These situations often involve low-level operations, optimization, or efficient memory management. Below are some real-life examples and scenarios where bitwise operators are used:

# 1. Flags and Bit Masks
# Bitwise operators are widely used in systems that need to represent a set of boolean values (true/false) using a single integer. This is often done using bit masking, where each bit represents a specific flag or condition.

# Real-Life Example:

# File permissions in Unix-based systems (Linux, macOS) use bitwise operations to store read, write, and execute permissions for files. Each permission can be represented by a single bit, and bitwise operators are used to check or modify these permissions.
# Example: File permissions using bitwise OR and AND

# Representing file permissions as bits:
# Read = 4 (binary 100)
# Write = 2 (binary 010)
# Execute = 1 (binary 001)

read_permission = 4  # 100
write_permission = 2  # 010
execute_permission = 1  # 001

# Combine permissions using bitwise OR
user_permissions = read_permission | write_permission  # 110 (read + write)

# Check if a permission is set using bitwise AND
if user_permissions & read_permission:  # 110 & 100 = 100, not zero => read permission is granted
    print("Read permission granted")
# Use case in operating systems: This method allows efficient checking and setting of individual bits to manage various flags, such as whether a file is readable, writable, or executable.

# 2. Network Programming (IP Address Subnetting)
# In networking, subnetting is used to divide an IP network into smaller subnetworks. This often involves using bitwise operations to manipulate IP addresses and subnet masks. Bitwise AND and OR operators are used to determine whether an IP address is part of a particular subnet.

# Example: Checking if an IP is within a certain subnet

# IP address and subnet mask in binary
ip = 0b11000000101010000000000100000001  # 192.168.1.1 in binary
subnet_mask = 0b11111111111111110000000000000000  # 255.255.0.0 in binary

# Check if the IP address belongs to the subnet
network_address = ip & subnet_mask  # Perform bitwise AND
print(bin(network_address))  # The network address is the masked IP address
# Use case in networking: This allows efficient routing and IP address management in large networks.

# 3. Cryptography and Data Security
# Bitwise operations are essential in cryptography algorithms such as XOR encryption and hashing algorithms. XOR, in particular, is often used for simple encryption/decryption due to its reversible nature.

# Example: XOR encryption/decryption

def xor_encrypt_decrypt(data, key):
    return data ^ key  # XOR encryption or decryption

# Example data and key (as integers)
data = 0b10101010  # Example data
key = 0b11001100   # Example key

# Encrypt
encrypted = xor_encrypt_decrypt(data, key)
print(f"Encrypted: {bin(encrypted)}")

# Decrypt (same operation as encryption)
decrypted = xor_encrypt_decrypt(encrypted, key)
print(f"Decrypted: {bin(decrypted)}")
# Use case in security: XOR encryption is commonly used in cryptographic applications, especially in situations where efficiency is a concern 
# (e.g., in low-level hardware security or simple encryption schemes).

# 4. Efficient Data Storage (Compression)
# In situations where memory is limited, such as in embedded systems, bitwise operations are used to store multiple boolean values (like flags or settings) 
# in a single integer, which saves memory. Compression algorithms sometimes use bitwise operations to manipulate data efficiently.

# Example: Storing multiple boolean values in a single integer

# Using an integer to store multiple boolean flags
settings = 0  # Start with all flags set to False (binary: 0000)

# Set the first and third flags to True (binary: 0101)
settings |= (1 << 0)  # Set the first bit (0001)
settings |= (1 << 2)  # Set the third bit (0100)

# Check if the second flag is True (binary: 0010)
if settings & (1 << 1):
    print("Second flag is True")
else:
    print("Second flag is False")
# Use case in data compression: Storing multiple boolean flags in a compact form using a single integer can reduce memory usage and improve performance 
# in constrained environments, such as IoT devices or mobile applications.

# 5. Graphics Programming (Pixel Manipulation)
# In graphics programming, bitwise operations are used for manipulating pixels in an image or creating color effects. For instance, each pixel's 
# color is often represented as a 24-bit value (8 bits for red, green, and blue channels), and bitwise operators are used to manipulate the color channels.

# Example: Manipulating color channels using bitwise operators

# 24-bit RGB color (8 bits per channel)
color = 0b111000111000000000111000  # RGB: (7, 0, 7) = Red: 7, Green: 0, Blue: 7

# Extract the red channel (first 8 bits)
red = (color >> 16) & 0xFF  # Right shift by 16 and mask the last 8 bits
print(f"Red channel: {red}")

# Extract the green channel (middle 8 bits)
green = (color >> 8) & 0xFF  # Right shift by 8 and mask the last 8 bits
print(f"Green channel: {green}")

# Extract the blue channel (last 8 bits)
blue = color & 0xFF  # Mask the last 8 bits
print(f"Blue channel: {blue}")
# Use case in graphics: This is crucial in game development, image processing, and other graphical applications where individual pixel manipulation is required.

# 6. Performance Optimization in Game Development
# In game development, bitwise operations are used for collision detection, masking, and state management to improve performance. 
# For example, in a game where multiple items or characters have different attributes, bitwise operations allow for efficient storage and checking of these attributes.

# Example: Optimizing character states using bitwise flags

# Each bit represents a different state of a game character
# 0001 = Alive, 0010 = Has Shield, 0100 = Is Jumping, 1000 = Has Power-Up

character_state = 0b0101  # Character has Shield and is Jumping (binary: 0101)

# Check if the character has a shield (bit 1)
if character_state & 0b0010:
    print("Character has a shield")

# Check if the character is jumping (bit 2)
if character_state & 0b0100:
    print("Character is jumping")
# Use case in gaming: This allows developers to efficiently store and check multiple state attributes of game entities, improving memory and performance.

# Conclusion:
# Bitwise operators are powerful tools that can optimize performance, especially in memory-constrained environments or when handling low-level data manipulation. Some common real-life applications of bitwise operators include:

# Flags and permissions (file system or security protocols)
# Network programming (subnetting and IP address calculations)
# Cryptography (simple encryption)
# Efficient data storage (compression and flag handling)
# Graphics programming (pixel manipulation)
# Game development (state management and collision detection)
# These applications leverage the efficiency of bitwise operations to perform tasks that would be cumbersome or less efficient using other methods.

x=10
y=8

print(bin(x),bin(y))
print(bin(x&y),x&y)
print(bin(x|y),x|y)
print(bin(x^y),x^y)