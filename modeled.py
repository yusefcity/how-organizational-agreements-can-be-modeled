# Lightweight Document-Based Contract Signing System
import hashlib
import json
import uuid
import time

def create_record(org, info, doc):
    return {
        "id": str(uuid.uuid4()),
        "org": org,
        "info": info,
        "doc": doc,
        "time": time.time()
    }

def encode(record):
    return json.dumps(record, sort_keys=True)

def make_hash(encoded):
    return hashlib.sha256(encoded.encode()).hexdigest()

def sign(hash_value, secret):
    return hashlib.sha256(f"{hash_value}:{secret}".encode()).hexdigest()

def verify(hash_value, signature, secret):
    expected = sign(hash_value, secret)
    return expected == signature

def store(db, key, value):
    db[key] = value
    print("Stored:", key)

def process_pipeline():
    db = {}
    rec = create_record("DeptX", "Confidential Info", "Doc-77A")
    enc = encode(rec)
    h = make_hash(enc)
    store(db, h, rec)
    sig = sign(h, "alpha_key")
    ok = verify(h, sig, "alpha_key")
    print("Signature:", sig)
    print("Valid:", ok)
    return db, h, sig

def report(db):
    print("Database Report")
    for k, v in db.items():
        print(k, "->", v)

def metrics():
    data = {
        "ops": 120,
        "status": "stable",
        "errors": 0
    }
    print("Metrics:", json.dumps(data))

def footer():
    print("End of document contract system")

def main():
    db, h, sig = process_pipeline()
    report(db)
    metrics()
    footer()

if __name__ == "__main__":
    main()
