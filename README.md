<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Logo -->
<br />
<div align="center">
  <a href="https://github.com/danielTunwashe/PizzaAPI">
    <img src="./Images/main-pic.jpeg" alt="Logo" width="90%" height="30%">
  </a>
</div>

<div align="center">
  <h1>PIZZA API</h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/danielTunwashe/PizzaAPI/issues#readme"><strong>Explore the Docs »</strong></a>
    <br />
    <a href="https://flask-pizza-delivery-api-app.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/danielTunwashe/PizzaAPI/issues">Report Bug</a>
    ·
    <a href="https://github.com/danielTunwashe/PizzaAPI/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-PizzaAPI">About PizzaAPI</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#lessons-learned">Lessons Learned</a></li>
    <li><a href="#usage">Usage</a></li>    
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the Blog -->
## About PizzaAPI

PizzaAPI is an API built on Flask-RESTX framework and properly documented in swagger UI. This API consists of various endpoints such as authentication, signup, retrieving all orders etc.

This pizza delivery API was built by <a href="https://www.github.com/danielTunwashe">Daniel Tunwashe</a> during Backend Engineering live classes at <a href="https://altschoolafrica.com/schools/engineering">AltSchool Africa</a>.

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Lessons Learned

Creating this API helped me learn and practice:
* API Development
* App Deployment with Heroku
* Testing
* Documentation
* Debugging
* Routing
* Database Management
* Internet Security
* User Authentication
* User Authorization
* Swagger UI Documentation

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- GETTING STARTED -->
## Usage

To use this API, follow these steps:

1. Open the Heroku app on your browser: https://flask-pizza-delivery-api-app.herokuapp.com/

2. Click 'auth' to reveal a dropdown menu of authentication routes

3. Register via the '/auth/signup' route, if you are a new user

4. Sign in via the '/auth/login' route to generate a JWT token. Copy this access token without the quotation marks

5. Scroll up to click "Authorize" at top right. Enter the JWT token in the given format, for example:
   ```
   Bearer this1is2a3rather4long5hex6string
   ```

6. Click 'Authorize' and then 'Close'

7. Now authorized, you can create, view, update and delete orders via the many routes in 'orders'

8. When you're done, click 'Authorize' at top right again to then 'Logout'

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->
## Sample

<br />

[![AltSchool Pizza Screenshot][altschool-pizza-screenshot]](https://github.com/danielTunwashe/PizzaAPI/blob/main/Images/sample.png)

<br/>

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/danielTunwashe/PizzaAPI/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

Daniel Tunwashe - [@danielTunwashe](https://twitter.com/DTunwashe) - tunwashed@gmail.com

Project Link: [PizzaAPI](https://github.com/danielTunwashe/PizzaAPI)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)
* [GitHub Student Pack](https://education.github.com/globalcampus/student)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/Ze-Austin/altschool-pizza.svg?style=for-the-badge
[contributors-url]: https://github.com/Ze-Austin/altschool-pizza/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Ze-Austin/altschool-pizza.svg?style=for-the-badge
[forks-url]: https://github.com/Ze-Austin/altschool-pizza/network/members
[stars-shield]: https://img.shields.io/github/stars/Ze-Austin/altschool-pizza.svg?style=for-the-badge
[stars-url]: https://github.com/Ze-Austin/altschool-pizza/stargazers
[issues-shield]: https://img.shields.io/github/issues/Ze-Austin/altschool-pizza.svg?style=for-the-badge
[issues-url]: https://github.com/Ze-Austin/altschool-pizzaissues
[license-shield]: https://img.shields.io/github/license/Ze-Austin/altschool-pizza.svg?style=for-the-badge
[license-url]: https://github.com/Ze-Austin/altschool-pizza/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@ze_austin-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/ze_austin
[twitter-url]: https://twitter.com/ze_austin
[altschool-pizza-screenshot]: https://github.com/Ze-Austin/altschool-pizza/blob/main/Images/screenshot.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
