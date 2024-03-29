<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://raw.githubusercontent.com/Nathaniel-github/CombinedServerClientRepo/main/TrieCLI/imgs/trie.png">
    <img src="https://raw.githubusercontent.com/Nathaniel-github/CombinedServerClientRepo/main/TrieCLI/imgs/trie.png" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Trie Client</h3>

  <p align="center">
    The client CLI for my globally hosted trie through GCP
    <br />
    <a href="https://trieclient.readthedocs.io/en/latest/index.html"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://pypi.org/project/trie-nathaniel/">View on PyPi</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



### Built With

* [inquirer.py](https://pypi.org/project/inquirer/)
* [click.py](https://pypi.org/project/click/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Install the CLI to get started!. Take a look at the <a href="#installation">Installation</a> section for the command to install.

### Prerequisites

Requires python>=3.6 and pip
  ```sh
sudo apt-get update
sudo apt-get install python3.6
  ```

NOTE: As it currently stands python 3.10 is not supported due to how inquirer's requirements are built in terms of blessed (it is using the wrong version)

<div id="installation"></div>

### Installation

Run the following to install:

```python
pip install trie-nathaniel==1.0.0
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

For clean user interface use:
```
triecli ui
```

For direct cli calls use:
```
triecli {option} {arg}
```
where `{option}` is replaced with the type of operation you would like to perform and `{arg}` is added if the option you are calling requires an argument

Possible options include `add`, `delete`, `deleteall`, `search`, `complete`, `view`, and `viewfast`

For `add`, `delete`, `search`, `complete` an additional `arg` parameter is required that includes the value you would like to add to the trie

LIMITATIONS:

The virtual machine this is running on only has 100GB of disk space and 4GB of memory so if the string is too long or the number of operations is too many there are chances that something will fail on the GCP side. Since this is being hosted using their free tier these are some of the limiations included

_For explanations, please refer to the [Documentation](https://trieclient.readthedocs.io/en/latest/index.html)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best README](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Nathaniel-github/CombinedServerClientRepo.svg?style=for-the-badge
[contributors-url]: https://github.com/Nathaniel-github/CombinedServerClientRepo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Nathaniel-github/CombinedServerClientRepo.svg?style=for-the-badge
[forks-url]: https://github.com/Nathaniel-github/CombinedServerClientRepo/network/members
[stars-shield]: https://img.shields.io/github/stars/Nathaniel-github/CombinedServerClientRepo.svg?style=for-the-badge
[stars-url]: https://github.com/Nathaniel-github/CombinedServerClientRepo/stargazers
[issues-shield]: https://img.shields.io/github/issues/Nathaniel-github/CombinedServerClientRepo.svg?style=for-the-badge
[issues-url]: https://github.com/Nathaniel-github/CombinedServerClientRepo/issues
[license-shield]: https://img.shields.io/github/license/Nathaniel-github/CombinedServerClientRepo.svg?style=for-the-badge
[license-url]: https://github.com/Nathaniel-github/CombinedServerClientRepo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/nathaniel-thomas-profile