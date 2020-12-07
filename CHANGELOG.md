# Changelog for WebMonitor

### 07 Dec 2020 (v 1.0.2)
#### Critical
* A JSONDecodeError was thrown while creating the file. Fixed by creating data model in init method.

### 05 Dec 2020 (v 1.0.1)
#### Critical
* Remove parameter `TIME_FORMAT` for __class__
* Remove parameter `force_check` for method `check()`
* Reformat configure file to json
* Create structured configure file
* Add responses input for remove actions
* Add Exceptions for logic

#### Notice
* Used JSON format for supported other languages
* Show hosts from file as table formatted

#### Back-stage
* Create private method for format input types
* For method `add()` change tuple type to list (format input types)
* Add structured history
* Added filter for history
* Make private variables and methods
* Refactor blocks code
* Code optimization
* Extend code pydoc for methods

#### Other
* Updated readme
* Added version control
* Added changelog
