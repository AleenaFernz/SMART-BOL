// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";
import {SmartBOL} from "../src/SmartBOL.sol";

contract SmartBOLTest is Test {

    SmartBOL smartBOL;

    address user = address(1);
    bytes32 sampleHash = keccak256("sample-document");

    function setUp() public {
        smartBOL = new SmartBOL();
    }

    function testMintSuccess() public {

        smartBOL.mint(user, sampleHash);

        assertEq(smartBOL.ownerOf(1), user);
        assertEq(smartBOL.documentToToken(sampleHash), 1);
    }

    function testDuplicateMintFails() public {

        smartBOL.mint(user, sampleHash);

        vm.expectRevert("Duplicate document");

        smartBOL.mint(user, sampleHash);
    }
}