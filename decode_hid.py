#!/usr/bin/env python3
# decode_hid.py
# Usage: python3 decode_hid.py hid_raw.txt
# Expects lines where last column contains the hex bytes for usb.capdata
# (e.g. output of: tshark -T fields -e frame.number -e usb.capdata ...)
import sys

# minimal HID keycode -> char map (US layout)
hid_map = {
    0x04: 'a',0x05: 'b',0x06: 'c',0x07: 'd',0x08: 'e',0x09: 'f',0x0a: 'g',0x0b: 'h',
    0x0c: 'i',0x0d: 'j',0x0e: 'k',0x0f: 'l',0x10: 'm',0x11: 'n',0x12: 'o',0x13: 'p',
    0x14: 'q',0x15: 'r',0x16: 's',0x17: 't',0x18: 'u',0x19: 'v',0x1a: 'w',0x1b: 'x',
    0x1c: 'y',0x1d: 'z',
    0x1e: '1',0x1f: '2',0x20: '3',0x21: '4',0x22: '5',0x23: '6',0x24: '7',0x25: '8',
    0x26: '9',0x27: '0',
    0x28: '\n',   # Enter
    0x2a: '[BACKSPACE]',
    0x2b: '\t',
    0x2c: ' ',    # Space
    0x2d: '-',0x2e: '=',0x2f: '[',0x30: ']',0x31: '\\',
    0x33: ';',0x34: "'",0x35: '`',0x36: ',',0x37: '.',0x38: '/',
}

# shifted symbols for numbers and punctuation when Shift pressed
shift_map = {
    '1': '!', '2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')',
    '-':'_','=':'+','[':'{',']':'}','\\':'|',';':':',"'":'"','`':'~',',':'<','.':'>','/':'?'
}

def is_shift(modbyte):
    # left shift = 0x02, right shift = 0x20
    return (modbyte & 0x22) != 0

def decode_keycode(kc, shift):
    if kc == 0:
        return None
    ch = hid_map.get(kc)
    if not ch:
        return f'[KC_{kc:02x}]'
    if shift:
        if ch.isalpha():
            return ch.upper()
        return shift_map.get(ch, ch)
    return ch

def parse_hex_bytes(hexstring):
    # hexstring might contain spaces already or be continuous
    parts = [p for p in hexstring.strip().split() if p]
    try:
        return [int(x,16) for x in parts]
    except:
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 decode_hid.py hid_raw.txt")
        sys.exit(1)
    infile = sys.argv[1]
    last_pressed = set()
    output = []
    with open(infile,'r',encoding='utf8',errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            # assume last column is the hex bytes; try to find it
            parts = line.split()
            # search for first token that looks like hex byte (2 hex chars)
            # simpler: take last N tokens that are hex-like
            hex_tokens = []
            for tok in parts[::-1]:
                if all(c in "0123456789abcdefABCDEF" for c in tok) and (len(tok) % 2 == 0):
                    # it's a run; split into bytes if necessary
                    # but many tshark outputs already space-separated bytes
                    # so we prefer tokens that are exactly 2 hex chars -> bytes
                    if len(tok) == 2:
                        hex_tokens.insert(0, tok)
                    else:
                        # maybe contiguous; split in pairs
                        pairs = [tok[i:i+2] for i in range(0,len(tok),2)]
                        hex_tokens = pairs + hex_tokens
                else:
                    # stop when last token isn't hex
                    if hex_tokens:
                        break
            if not hex_tokens:
                # fallback: take last token and split
                hex_tokens = [p for p in parts[-1].split() if p]
            bytes_list = parse_hex_bytes(' '.join(hex_tokens))
            if len(bytes_list) < 3:
                continue
            mod = bytes_list[0]
            # reserved = bytes_list[1]
            keycodes = bytes_list[2:]
            # consider any nonzero keycode as pressed; many keyboards send 6-key rollover => keycodes list up to 6
            pressed = {k for k in keycodes if k != 0}
            # Determine newly pressed keys (present now, not present previously)
            new = pressed - last_pressed
            # Determine released keys if needed (not used to output)
            #releases = last_pressed - pressed
            # For each newly pressed key, output character (taking shift into account)
            for kc in sorted(new):
                ch = decode_keycode(kc, is_shift(mod))
                if ch is not None:
                    output.append(ch)
            last_pressed = pressed
    # join output and print
    reconstructed = ''.join(output)
    print(reconstructed)

if __name__ == '__main__':
    main()