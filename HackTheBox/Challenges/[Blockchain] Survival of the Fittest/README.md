# Survival of the Fittest
`function call` `foundry` `cast`
<br>
<br>

We were given two solidity code, `Setup.sol`and `Creature.sol`, the code is as below

**Creature.sol**
```javascript
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Creature {
    
    uint256 public lifePoints;
    address public aggro;

    constructor() payable {
        lifePoints = 20;
    }

    function strongAttack(uint256 _damage) external{
        _dealDamage(_damage);
    }
    
    function punch() external {
        _dealDamage(1);
    }

    function loot() external {
        require(lifePoints == 0, "Creature is still alive!");
        payable(msg.sender).transfer(address(this).balance);
    }

    function _dealDamage(uint256 _damage) internal {
        aggro = msg.sender;
        lifePoints -= _damage;
    }
}
```

**Setup.sol**
```javascript
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Creature} from "./Creature.sol";

contract Setup {
    Creature public immutable TARGET;

    constructor() payable {
        require(msg.value == 1 ether);
        TARGET = new Creature{value: 10}();
    }
    
    function isSolved() public view returns (bool) {
        return address(TARGET).balance == 0;
    }
}
```

This challenge is count as a very basic Blockchain challenge, an introductory if you will, so, the challenge creator create a `/documentation` on how you can solve this challenge, as for the connection, is right on the `/connections`, by calling to this endpoint we can get the `private_key`, `address(wallet)`, `target address` and `setup address`.

The one we will working with is the `Creature.sol`, why you might ask, the function there is used in the Setup contract, that's why we are going to work with it.

A short explanation here about the fuctions and variables there
```
lifePoint             -> Monster HP
strongAttack(uint256) -> Attack with desired damage
punch()               -> Attack with 1 damage
loot()                -> Once the monster Die, we can loot to get the flag
_dealDamage()         -> Private Function that will do damage to the monster
```

Seeing the available options above, we can choose 2 methods to kill the monster, we can either kill the monster by calling `punch()` 20 times, since the Monster HP is 20, or we can call `strongAttack(uint256)` once with the damage value of 20 to instantly kill ke monster.

Let's learn how to call the function using [Foundry](https://book.getfoundry.sh/getting-started/installation), this one we gonna use is [cast](https://book.getfoundry.sh/cast/). The concept is quite simple actually, if we need to change/insert an input, we use 

```bash
cast send --rpc-url <http-rpc> --private-key <priv-key> <target-addr> "<function>" <input>
```

But if we only need to call a function without changing anything, we can simply use 

```bash
cast call --rpc-url <http-rpc> <target-addr> "<function>"
```

Since we have the option to kill the monster in a single hit using `strongAttack(uint256)` function, we can simply deal 20 damage in an instant then call the `loot()` function to get our flag (and trigger the `isSolved()` function).

```bash
#Check lifePoints
cast call --rpc-url <http-rpc> <target-addr> "lifePoints()" 

#Deal 20 Damage
cast send --rpc-url <http-rpc> --private-key <priv-key> <target-addr> "strongAttack(uint256)" 20 

#Check lifePoints (make sure it went down to 0)
cast call --rpc-url <http-rpc> <target-addr> "lifePoints()" 

#Loot
cast call --rpc-url <http-rpc> --private-key <priv-key> <target-addr> "loot()"
```

After this we just need to go to the `/flag` endpoint to get our flag.