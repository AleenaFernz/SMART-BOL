import { useState } from "react";
import { connectWallet } from "./web3";
import { BrowserProvider, Contract, keccak256, toUtf8Bytes } from "ethers";
import { CONTRACT_ADDRESS, CONTRACT_ABI } from "./contract";

function App() {
  const [address, setAddress] = useState<string | null>(null);
  const [provider, setProvider] = useState<BrowserProvider | null>(null);
  const [ownedTokens, setOwnedTokens] = useState<number[]>([]);

  const handleConnect = async () => {
    try {
      const { provider, address } = await connectWallet();
      setProvider(provider);
      setAddress(address);
      await loadOwnedTokens();
    } catch (error) {
      console.error(error);
    }
  };

  const handleMint = async () => {
  if (!provider || !address) return;

  try {
    const signer = await provider.getSigner();

    const contract = new Contract(
      CONTRACT_ADDRESS,
      CONTRACT_ABI,
      signer
    );

    const documentHash = keccak256(
      toUtf8Bytes("sampl")
    );

    const tx = await contract.mint(address, documentHash);

    await tx.wait();

    await loadOwnedTokens();

    alert("Mint successful!");

  } catch (error: any) {
    console.error(error);

    // 🔎 Detect duplicate revert
    if (
      error?.reason === "Duplicate document" ||
      error?.info?.error?.message?.includes("Duplicate document")
    ) {
      alert("Duplicate document detected. This BoL already exists.");
    } //else {
      //alert("Mint failed. See console for details.");
    //}
  }
};

  const loadOwnedTokens = async () => {
  if (!provider || !address) return;

  const signer = await provider.getSigner();

  const contract = new Contract(
    CONTRACT_ADDRESS,
    CONTRACT_ABI,
    signer
  );

  const tokens = await contract.tokensOfOwner(address);

  setOwnedTokens(tokens.map((t: any) => Number(t)));
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
          
          <h3>Owned BoLs</h3>

{ownedTokens.length === 0 ? (
  <p>No BoLs owned</p>
) : (
  <ul>
    {ownedTokens.map((token) => (
      <li key={token}>BoL Token ID: {token}</li>
    ))}
  </ul>
)}
        </div>
      )}
    </div>
  );
}

export default App;