# Game modifications

Load for changing an existing game, not a standalone browser game. Establish game/platform/version, desired action and multiplayer context from project files before asking.

Prefer supported configuration/content packs, editors or scripting to compiled mods when sufficient. Engine name alone does not prove mod support. Verify API signatures and loader compatibility from accessible maintainer docs or assemblies; never invent runnable methods.

For multiplayer, distinguish local visuals from authoritative state/replication. Track object identity and confirmed transitions; repeated input must not duplicate effects. Host/client installation requirements need evidence, not guesses.

Build in a separate directory. Installing into the game, changing saves or joining sessions requires the relevant authorization; preserve permission already given. Missing game/tools means explicit blockers and verified preparation, not “in-game success” based on stubs.

Sources: game mod docs, loader/framework maintainer docs and actual assembly/project signatures. Accept with compile/logic checks followed by in-game and multiplayer tests when available; label each level separately. Stop at the verified level or exact missing access; do not research unrelated platforms.
