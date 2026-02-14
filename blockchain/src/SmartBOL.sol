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

       function totalMinted() public view returns (uint256) {
        return _nextTokenId;
    }

    function tokensOfOwner(address owner) public view returns (uint256[] memory) {

        uint256 total = _nextTokenId;
        uint256 count = balanceOf(owner);

        uint256[] memory result = new uint256[](count);

        uint256 index = 0;

        for (uint256 i = 1; i <= total; i++) {
            if (ownerOf(i) == owner) {
                result[index] = i;
                index++;
            }
        }

        return result;
    }

}