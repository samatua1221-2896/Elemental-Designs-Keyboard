from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC

keyboard = KMKKeyboard()

# Row and Column Pins (from your schematic)
keyboard.row_pins = (keyboard.gp0, keyboard.gp1, keyboard.gp2, keyboard.gp3, keyboard.gp4, keyboard.gp5)
keyboard.col_pins = (keyboard.gp6, keyboard.gp7, keyboard.gp8, keyboard.gp9,
                     keyboard.gp10, keyboard.gp11, keyboard.gp12, keyboard.gp13,
                     keyboard.gp14, keyboard.gp15, keyboard.gp16, keyboard.gp17,
                     keyboard.gp18, keyboard.gp19)

# Diode Direction (assuming COL2ROW from your schematic)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder Setup
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder Pins (based on schematic SW6 and SW7)
encoder_handler.pins = (
    (keyboard.gp20, keyboard.gp21),  # Encoder 1 - Volume
    (keyboard.gp22, keyboard.gp26),  # Encoder 2 - Custom Scroll
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU), KC.MUTE),  # Encoder 1 rotation and press
    ((KC.PGDN, KC.PGUP), KC.NO),    # Encoder 2 rotation and press (customizable later)
]

# Keymap Layout (Standard Full Size w/o F-Row and PgUp/PgDn)
keyboard.keymap = [
    [
        # Row 0 (Example: Esc, `, 1-0, -, =, Backspace)
        KC.ESC, KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
        KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC,
        
        # Row 1 (Tab, Q-P, [, ], \)
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U,
        KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,
        
        # Row 2 (Caps, A-L, ;, ', Enter)
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H,
        KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,
        
        # Row 3 (LShift, Z-M, ,, ., /, RShift)
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N,
        KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        
        # Row 4 (LCtrl, LGUI, LAlt, Space, RAlt, RGUI, Menu, RCtrl)
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL,
        
        # Extra keys (Arrow Keys, Delete, Home, End, Insert)
        KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT, KC.DEL, KC.HOME, KC.END, KC.INS
    ]
]

if __name__ == '__main__':
    keyboard.go()
