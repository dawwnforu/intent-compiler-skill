# Physical-size print layouts

Load for photos/labels/pages that need real printed dimensions, not screen galleries or 3D fabrication. Determine paper, margins, physical image size and crop/stretch preference from inputs; use reversible visual defaults.

Preview pixels are not millimeters. Keep one physical layout for preview/export; convert to the output format's units rather than screen DPI. Preserve aspect ratio unless distortion is requested. Rotation changes occupied size; cropping is distinct from scaling. Oversize content needs explicit handling, not silent clipping.

Photo quantity and unique images differ: duplicate cleanup must not erase requested copies. Reflow and export must use current state.

Validate print quantities separately from physical dimensions. Copies are nonnegative integers: zero omits that record from this batch without deleting it from the reusable list, unless the supplied workflow explicitly forbids zero. Reject fractional or negative copies. Label width/height must be positive; margins and gaps must meet the supplied minimums. If all copies are zero, report that there is nothing to print and do not export stale labels from a previous batch. Verify a zero-copy omission and a later positive count using current data.

Sources: chosen PDF library's official unit/image docs, actual image dimensions and paper specification. A DPI label alone does not guarantee sharpness; original pixels constrain usable resolution.

Accept by checking page dimensions and physical placements, a known-size example, overlap/bounds and preview/export agreement after resizing/rotation. Inspect the actual PDF when possible; distinguish digital checks from physical printing. Stop after relevant output checks.
