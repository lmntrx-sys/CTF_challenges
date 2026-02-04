from winterbucks_confession import WinterBucks, _hidden_in_snow, main
import base64

def decrypt_confession(data):
    """Reverse the _avalanche_encryption process"""
    # Step 1: Reverse the data (undo the reversal)
    _SNOW_DEPTH = "BBV_p>7^l97gtW]jVGX_7>LglpJN;97guS8hq_rg{SLN~[Lizq7ilp]Y"
    layer1 = _SNOW_DEPTH[::-1]
    print(f"Layer 1 (reversed): {layer1}")
    
    # Step 2: Subtract 5 from each character (undo the shift)
    layer2 = ''.join([chr(ord(c) - 5) for c in layer1])
    print(f"Layer 2 (shifted back): {layer2}")
    
    # Step 3: Base64 decode (undo the base64 encoding)
    layer3 = base64.b64decode(layer2).decode()
    
    return layer3



if __name__ == "__main__":
    wb = WinterBucks()
    confession = input("Enter your confession: ")
    print(f"VERIFYING CONFESSION... {wb.verify_confession(decrypt_confession(confession))}")
    