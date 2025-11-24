import requests, time

def void_scream():
    print("Aptos — The Void Screams When Big Money Dies")
    seen = set()
    while True:
        r = requests.get("https://api.mainnet.aptoslabs.com/v1/transactions?limit=30")
        for tx in r.json():
            h = tx.get("hash")
            if not h or h in seen: continue
            seen.add(h)
            if tx.get("success") or tx.get("vm_status") != "EXECUTION_FAILURE": continue
            
            payload = tx.get("payload", {})
            if payload.get("function") != "0x1::coin::transfer": continue
            
            amount = int(tx.get("changes", [{}])[0].get("data", {}).get("value", "0"))
            if amount > 10_000_000_000:  # >10M APTOS (~$100M+ at peak)
                print(f"THE VOID JUST SCREAMED\n"
                      f"Someone burned ${amount/1e8 * 8:,.0f} trying to move it\n"
                      f"Failed tx: {h}\n"
                      f"Sender: {tx['sender'][:16]}...\n"
                      f"https://explorer.aptoslabs.com/txn/{tx['version']}\n"
                      f"→ Greed met the speed of light and lost\n"
                      f"→ This is what overconfidence sounds like at 100k TPS\n"
                      f"{'▣ ▢ ▣ ▢'*25}\n")
        time.sleep(1.9)

if __name__ == "__main__":
    void_scream()
