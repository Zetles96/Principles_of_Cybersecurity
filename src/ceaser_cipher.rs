fn encrypt(plain_text: &str, shift: u8) -> String {
    let mut cipher_text = String::new();
    for char in plain_text.chars() {
        if !char.is_ascii_alphanumeric() {
            cipher_text.push(char);
            continue;
        }
        let base = if char.is_ascii_uppercase() { 'A' as u8 } else { 'a' as u8 };
        let shifted_char = ((char as u8 - base + shift) % 26 + base) as char;
        cipher_text.push(shifted_char)
    }
    return cipher_text;
}

fn decrypt(cipher_text: &str, shift: u8) -> String {
    let mut plaint_text = String::new();
    for char in cipher_text.chars() {
        if !char.is_ascii_alphanumeric() {
            plaint_text.push(char);
            continue;
        }
        let base = if char.is_ascii_uppercase() { 'A' as u8 } else { 'a' as u8 };
        let shifted_char = ((char as u8 - base + 26 - shift) % 26 + base) as char;
        plaint_text.push(shifted_char)
    }
    return plaint_text;
}

fn decrypt_all(cipher_text: &str) {
    for i in 0..26 {
        let decrypted = decrypt(cipher_text, i);
        println!("{i}:\t{decrypted}")
    }
}

fn main() {
    let cipher_text = "Jmpwfzpv4111";
    decrypt_all(cipher_text);
}