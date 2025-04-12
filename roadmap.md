operation-obscura/
│
├── main.py
├── agent/
│   ├── __init__.py
│   ├── generator.py         # Creates fake agents
│   └── credentials.py       # Encrypts/decrypts agent credentials
│
├── mission/
│   ├── __init__.py
│   ├── log_simulator.py     # Creates fake surveillance logs
│   ├── decryptor.py         # Fake mission file decryptor
│   └── mission_data.txt     # Hidden hints
│
├── utils/
│   ├── __init__.py
│   ├── terminal_effects.py  # Typing animation & screen noise
│   └── cipher.py            # Simple Caesar/Vigenère ciphers
│
├── data/
│   ├── agents.json
│   ├── encrypted_logs.dat
│   └── readme_hidden.md
│
└── README.md
