// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC721} from "openzeppelin-contracts/contracts/token/ERC721/ERC721.sol";

contract SmartBOL is ERC721 {

    uint256 private _nextTokenId;

    // documentHash => tokenId
    mapping(bytes32 => uint256) public documentToToken;

    constructor() ERC721("SMART-BOL+", "SBOL") {}

    function mint(address to, bytes32 documentHash) external {

        require(documentToToken[documentHash] == 0, "Duplicate document");

        _nextTokenId++;

        uint256 newTokenId = _nextTokenId;

        _safeMint(to, newTokenId);

        documentToToken[documentHash] = newTokenId;
    }
}