# 📝 Random Teacher
<p align="center">
        <img src="images/random_teacher.png" alt="Random Teacher logo" width="600"/>
</p>

        An approach to generate random tests automatically.

One of the problems that hinder learning is cheating in assessments and exams. Researchers found that:
* 64 percent of students **admitted to cheating on a test**,
* 58 percent **admitted to plagiarism**,
* 95 percent said **they participated in some form of cheating** (1).

Although improving student morale is one avenue, we can look for ways that have a great impact and prevent a wide spectrum of cases. We start from the basic premise: *"A student who knows that he cannot cheat will be more willing to learn the right way"*.

This is how **📝 Random Teacher** arises, a code-based approach that allows you to create evaluations procedurally, that is, create random evaluations using algorithms written in python. 

## Advantages

* Create unique exercises for students or groups.
* Very difficult to copy through traditional strategies.
* Create new material periodically with minimal effort.
* Motivate students to learn by discouraging non-legal methods.
* Have a more objective measure of individual / group performance.




## How to use it?

* Clone the repo.
* Create the environment and install packages.

        python3 -m venv math_tests
        source math_tests/bin/activate
        python3 -m pip install -r requirements.txt

* Execute the random teacher command. With this instruction, we can generate the files for the statistics module `statistics_m1`

        python main.py --module statistics_m1

* Output

        ===== 📝 Random Teacher =====
                Creating module statistics_m1.
                10 new distributions were created with their solutions.
                Questions saved in: data/statistics_module1_questions.docx
                Answers saved in: data/statistics_module1_solutions.docx
                The module was created succesfully.

* If you **want to generate documents from all the available modules**, you can execute without specifying a module:

        python main.py

 The CLI will use a default argument 'all' to create all the modules.

## Result

An example of the expected result will be two documents. Solutions and Questions documents:

### Random questions

<p align="center">
        <img src="images/questions.png" alt="Random questions image" width="600"/>
</p>

### Random solutions

<p align="center">
        <img src="images/solutions.png" alt="Random solutions" width="600"/>
</p>


## List of available modules

* `statistics_m1`

## How to collaborate with the project

Every new module must be defined in a class that follows the interface `writer_interface.py`. The module must create new questions (or hard to repeat questions) every time is executed. You must read the interface to identify the logic for the methods. The requirements are:

* Create a fork of the repo.
* Your module must be defined inside a class in the `writers` folder.
* The class must be named following this format: `SubjectExampleModuleN`.
* The class must save the output documents in the `data` folder.
* It is not mandatory, but it is suggested to use the [python-docx](https://python-docx.readthedocs.io/en/latest/) module to create the documents in docx format.
* Add your new module to the dictionary in line 7 in `main.py` (in this example, your module is `SubjectExampleModuleN`):

        MODULES = {
                "statistics_m1": StatisticsModule1,
                "subject_example_module_n": SubjectExampleModuleN
                }
* Use [Flake8](https://flake8.pycqa.org/en/latest/) and [Black](https://black.readthedocs.io/en/stable/) packages for linting and autolinting.
* Your code must use [type hints](https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html).
* Document the code using the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) as reference. If you use VSCode, you can install the `Python Docstring Generator` extension and configure for Google style.
* Create a pull request from a fork with a branch named `subject_example_module_n`.

If it meets the requirements, the new module can be added to the list of modules available to be executed from the command line.

## References

[1] McCabe, D. L., Butterfield, K. D., & Trevino, L. K. (2012). Cheating in college: Why students do it and what educators can do about it. JHU Press.

## Notes

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

