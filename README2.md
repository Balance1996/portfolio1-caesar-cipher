#This is the second readme file on how to do caeszar cipher with function
Goal-
Create a Caesar Cipher program that performs encryption and decryption using a functional programming approach. 
The program separates responsibilities into specialized functions, with main() acting as the coordinator.

Features-
Encrypt text
Decrypt text
Supports custom shift amounts
Preserves spaces and punctuation
Wraps alphabet positions using modulo arithmetic (% 26)

What I learned-
Function responsibility
main() should coordinate the program.
encode_text() and decode_text() should own the transformation logic.
Helper functions
Helper functions can simplify repeated decisions.
Example: replacing char.isalpha() with validate_text(char) to separate validation from transformation.
Character-by-character processing
Loop through each character instead of validating the entire message.
Preserve spaces and special characters while only shifting alphabetic characters.
Modulo arithmetic
% 26 prevents alphabet positions from going out of range when shifting characters.
Building the output
Use a temporary string (such as txt) to gradually construct the encrypted or decrypted message.

Future Improvements-
Support uppercase letters.
Improve input validation.
Add automated unit tests.
Allow users to define additional characters to preserve or transform.
Refactor encryption and decryption into a single reusable Caesar cipher function
