# HFTE
Context: Supporting material for the paper "Guidelines for Building a Realistic Algorithmic Trading Market Simulator for Backtesting while Incorporating Market Impact" What it does: This is a simplification of the HFT game. We examine, in sequence how different classic financial strategies fair with respect to each other via an orderbook

About the file:
- HFTEgame: illustrates how simple strategies do when communicating through an orderbook
- HFTEgameRand and HFTEgameWithMarketMaker are slightly more advanced version of HFTEgame
- HFTE_PF illustrates how a particular Particle Filter can achieve tracking of the ecosystem. Note that this code may not work depending on python version. However a simple debuging should allow you investigate how to make it work
- plotInstability illustrates how the strategies when interacting with each other and mimick randomness  
