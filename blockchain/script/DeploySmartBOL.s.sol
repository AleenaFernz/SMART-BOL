// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Script} from "forge-std/Script.sol";
import {SmartBOL} from "../src/SmartBOL.sol";

contract DeploySmartBOL is Script {

    function run() external {

        vm.startBroadcast();

        new SmartBOL();

        vm.stopBroadcast();
    }
}