ABI_ZETA = '[{"inputs":[{"internalType":"address","name":"tssAddress_","type":"address"},{"internalType":"address","name":"tssAddressUpdater_","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"CallerIsNotConnector","type":"error"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"CallerIsNotTss","type":"error"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"CallerIsNotTssOrUpdater","type":"error"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"CallerIsNotTssUpdater","type":"error"},{"inputs":[],"name":"InvalidAddress","type":"error"},{"inputs":[],"name":"ZetaTransferError","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"burnee","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Burnt","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"mintee","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":true,"internalType":"bytes32","name":"internalSendHash","type":"bytes32"}],"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burnFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"connectorAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"mintee","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"bytes32","name":"internalSendHash","type":"bytes32"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceTssAddressUpdater","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tssAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tssAddressUpdater","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tssAddress_","type":"address"},{"internalType":"address","name":"connectorAddress_","type":"address"}],"name":"updateTssAndConnectorAddresses","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
ABI_SWAP = '[{"inputs":[{"internalType":"address","name":"zetaConnector_","type":"address"},{"internalType":"address","name":"zetaToken_","type":"address"},{"internalType":"address","name":"uniswapV3Router_","type":"address"},{"internalType":"address","name":"quoter_","type":"address"},{"internalType":"address","name":"WETH9Address_","type":"address"},{"internalType":"uint24","name":"zetaPoolFee_","type":"uint24"},{"internalType":"uint24","name":"tokenPoolFee_","type":"uint24"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"ErrorApprovingTokens","type":"error"},{"inputs":[],"name":"ErrorSendingETH","type":"error"},{"inputs":[],"name":"ErrorSwappingTokens","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"ErrorTransferringTokens","type":"error"},{"inputs":[],"name":"InputCantBeZero","type":"error"},{"inputs":[],"name":"InsufficientOutToken","type":"error"},{"inputs":[],"name":"InvalidAddress","type":"error"},{"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"InvalidCaller","type":"error"},{"inputs":[],"name":"InvalidDestinationChainId","type":"error"},{"inputs":[],"name":"InvalidMessageType","type":"error"},{"inputs":[],"name":"InvalidZetaMessageCall","type":"error"},{"inputs":[],"name":"InvalidZetaRevertCall","type":"error"},{"inputs":[],"name":"MissingSourceInputTokenAddress","type":"error"},{"inputs":[],"name":"OutTokenInvariant","type":"error"},{"inputs":[],"name":"ReentrancyError","type":"error"},{"inputs":[],"name":"ValueShouldBeGreaterThanZero","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"EthExchangedForZeta","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sourceTxOrigin","type":"address"},{"indexed":false,"internalType":"address","name":"sourceInputToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"inputTokenAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"inputTokenReturnedAmount","type":"uint256"}],"name":"RevertedSwap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sourceTxOrigin","type":"address"},{"indexed":false,"internalType":"uint256","name":"inputEthAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"destinationOutToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"outTokenMinAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"receiverAddress","type":"address"}],"name":"SentEthSwap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sourceTxOrigin","type":"address"},{"indexed":false,"internalType":"address","name":"sourceInputToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"inputTokenAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"destinationOutToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"outTokenMinAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"receiverAddress","type":"address"}],"name":"SentTokenSwap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sourceTxOrigin","type":"address"},{"indexed":false,"internalType":"address","name":"sourceInputToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"inputTokenAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"destinationOutToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"outTokenFinalAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"receiverAddress","type":"address"}],"name":"Swapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"TokenExchangedForZeta","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"ZetaExchangedForEth","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"token","type":"address"},{"indexed":false,"internalType":"uint256","name":"amountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amountOut","type":"uint256"}],"name":"ZetaExchangedForToken","type":"event"},{"inputs":[],"name":"CROSS_CHAIN_SWAP_MESSAGE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"connector","outputs":[{"internalType":"contract ZetaConnector","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"destinationAddress","type":"address"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"},{"internalType":"uint256","name":"zetaTokenAmount","type":"uint256"}],"name":"getEthFromZeta","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"destinationAddress","type":"address"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"},{"internalType":"address","name":"outputToken","type":"address"},{"internalType":"uint256","name":"zetaTokenAmount","type":"uint256"}],"name":"getTokenFromZeta","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"destinationAddress","type":"address"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"}],"name":"getZetaFromEth","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"destinationAddress","type":"address"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"},{"internalType":"address","name":"inputToken","type":"address"},{"internalType":"uint256","name":"inputTokenAmount","type":"uint256"}],"name":"getZetaFromToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"interactorsByChainId","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"zetaTxSenderAddress","type":"bytes"},{"internalType":"uint256","name":"sourceChainId","type":"uint256"},{"internalType":"address","name":"destinationAddress","type":"address"},{"internalType":"uint256","name":"zetaValue","type":"uint256"},{"internalType":"bytes","name":"message","type":"bytes"}],"internalType":"struct ZetaInterfaces.ZetaMessage","name":"zetaMessage","type":"tuple"}],"name":"onZetaMessage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"zetaTxSenderAddress","type":"address"},{"internalType":"uint256","name":"sourceChainId","type":"uint256"},{"internalType":"bytes","name":"destinationAddress","type":"bytes"},{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"uint256","name":"remainingZetaValue","type":"uint256"},{"internalType":"bytes","name":"message","type":"bytes"}],"internalType":"struct ZetaInterfaces.ZetaRevert","name":"zetaRevert","type":"tuple"}],"name":"onZetaRevert","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"quoter","outputs":[{"internalType":"contract IQuoter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"bytes","name":"contractAddress","type":"bytes"}],"name":"setInteractorByChainId","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes","name":"receiverAddress","type":"bytes"},{"internalType":"address","name":"destinationOutToken","type":"address"},{"internalType":"bool","name":"isDestinationOutETH","type":"bool"},{"internalType":"uint256","name":"outTokenMinAmount","type":"uint256"},{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"uint256","name":"crossChaindestinationGasLimit","type":"uint256"}],"name":"swapETHForTokensCrossChain","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"sourceInputToken","type":"address"},{"internalType":"uint256","name":"inputTokenAmount","type":"uint256"},{"internalType":"bytes","name":"receiverAddress","type":"bytes"},{"internalType":"address","name":"destinationOutToken","type":"address"},{"internalType":"bool","name":"isDestinationOutETH","type":"bool"},{"internalType":"uint256","name":"outTokenMinAmount","type":"uint256"},{"internalType":"uint256","name":"destinationChainId","type":"uint256"},{"internalType":"uint256","name":"crossChaindestinationGasLimit","type":"uint256"}],"name":"swapTokensForTokensCrossChain","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tokenPoolFee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV3Router","outputs":[{"internalType":"contract ISwapRouter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zetaPoolFee","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zetaToken","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'
RPC = [
    'https://data-seed-prebsc-1-s1.binance.org:8545',
    'https://rpc-mumbai.maticvigil.com'
]