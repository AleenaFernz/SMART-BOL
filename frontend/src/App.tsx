import { useState } from "react";
import { connectWallet } from "./web3";
import { BrowserProvider, Contract, keccak256, toUtf8Bytes } from "ethers";
import { CONTRACT_ADDRESS, CONTRACT_ABI } from "./contract";

function App() {
  const [address, setAddress] = useState<string | null>(null);
  const [provider, setProvider] = useState<BrowserProvider | null>(null);

  const handleConnect = async () => {
    try {
      const { provider, address } = await connectWallet();
      setProvider(provider);
      setAddress(address);
    } catch (error) {
      console.error(error);
    }
  };

  const handleMint = async () => {
    if (!provider || !address) return;

    const signer = await provider.getSigner();

    const contract = new Contract(
      CONTRACT_ADDRESS,
      CONTRACT_ABI,
      signer
    );

    // Simulate backend hash
    const documentHash = keccak256(toUtf8Bytes("sample-bol"));

    const tx = await contract.mint(address, documentHash);

    await tx.wait();

    alert("Mint successful!");
  };

  return (
    <div style={{ padding: "40px", fontFamily: "sans-serif" }}>
      <h1>SMART-BOL+</h1>

      {!address ? (
        <button onClick={handleConnect}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Wallet:</p>
          <strong>{address}</strong>

          <br /><br />

          <button onClick={handleMint}>
            Mint Sample BoL NFT
          </button>
        </div>
      )}
    </div>
  );
}

export default App;