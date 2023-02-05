## Changelog

#### `1.4.2` (2023-02-05)
- Corrected `fetools.geomath.sct2todd` to return the correct type (a tuple of floats, not strings)

#### `1.4.1` (2022-07-02)
#### `1.4.0` (2022-07-02)
- Add helper functions for converting between the NASR ddd-mm-ss.sssH format and decimal degrees to `fetools.geomath`
- In `fetools.geomath`, renamed `ddtodms` to `ddtosct2` and `dmstodd` to `sct2todd` (old names are still there just in case)

#### `1.3.0` (2021-08-05)
- Add tools for working with POF files (`fetools.pof`)

#### `1.2.1-post` (2021-02-21)
- Rename `fetools.alias.AliasCommands.dumpxml` to `fetools.alias.AliasCommands._dumpxml`

#### `1.2.1` (2021-02-16)
- Bug fixes to fetools.alias

#### `1.2.0` (2021-01-27)
- Add tools for working with alias files (`fetools.alias`)

#### `1.1.0` (2021-01-22)
- Add color converters

#### `1.0.2` (2021-01-18)
#### `1.0.1` (2021-01-17)
- Squash bugs

#### `1.0.0` (2021-01-17)
- Add some misc. helper functions
