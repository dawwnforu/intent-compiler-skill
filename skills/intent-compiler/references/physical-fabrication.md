# Physical fabrication and functional objects

## Applies and trigger
Load when the user intends to print, manufacture, assemble or physically use an object.

## Exclude
Do not load for visual-only rendering. Decorative fabrication does not automatically require mechanism design or a full structural engineering workflow.

## Prerequisites
Inspect dimensions and units, mating parts, intended use/environment, material, fabrication process and available machine/service constraints. Recover measurements from supplied files before asking. An unknown fit dimension or load is not a safe artistic default.

## Decisions
- Physical fit requires actual dimensions, orientation and process-appropriate tolerances; do not hard-code universal clearances.
- Load bearing, motion, heat or another stated functional demand makes the relevant mechanics, forces, connections and validation necessary. Establish load direction/magnitude, mounting substrate and attachment when applicable.
- A display model can be a draft reference; it is not automatically manufacturable. Mesh closure alone does not establish strength.
- Treat professional review or physical testing as a prerequisite when the intended use demands it; do not promise functional safety from rendering or an unvalidated simulation.

## Common omissions
Units can change object size dramatically. Material/process anisotropy, wall thickness, print orientation, mating clearances, fasteners and assembly access may change whether the requested object works. Explain the practical consequence: “This joint affects whether the parts fit; I need the mating measurement before fixing its dimensions.”

## Sources
Use measured drawings, project CAD notes and available CAD/3D skills first. Retrieve the selected machine/process vendor's technical guidance and material datasheet, and applicable engineering standards for the actual use. [Blender's 3D printing documentation](https://docs.blender.org/manual/en/latest/addons/mesh/3d_print_toolbox.html) is a potential mesh-check entry point; verify its availability for the installed version rather than assuming the add-on exists. Verify current service limits and applicable regional requirements at execution.

## Execute
Separate known dimensions from unresolved measurements. Build only the supported geometry; preserve unresolved values as explicit parameters/draft constraints. Inspect relevant manufacturability and assembly conditions, export for the chosen workflow, and perform available functional checks. Do not order fabrication or pay a vendor without matching authorization.

## Accept
Check scale/units, relevant geometry/manufacturability, mating/assembly constraints and export importability. Record which checks actually ran. For functional use, record load assumptions and validation evidence or the missing physical test/review. Label “draft, fit/strength unverified” where appropriate; do not label a render “ready to use”.

## Continue and stop
Retrieve mechanics only when actual function triggers it; retrieve process-specific constraints only for the selected process. Stop once relevant conditions and acceptance are clear. If essential measurements or test equipment are missing, stop dependent claims, deliver unaffected draft work, and state the next measurement/test needed.
