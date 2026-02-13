import { useState } from "react";
import { connectWallet } from "./web3";

function App() {
  const [address, setAddress] = useState<string | null>(null);

  const handleConnect = async () => {
    try {
      const { address } = await connectWallet();
      setAddress(address);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>SMART-BOL+</h1>

      {!address ? (
        <button onClick={handleConnect}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p>Connected Wallet:</p>
          <strong>{address}</strong>
        </div>
      )}
    </div>
  );
}

export default App;