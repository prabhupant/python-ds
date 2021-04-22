# Contributing

This is a project that is for the community and its true essence is only possible when it is community driven.

Please feel free to contribute to this project and be a part of this. Anything from raising issues to adding new features or even a typo in documentations, all are welcome. Please report issues here [https://github.com/prabhupant/python-ds/issues](https://github.com/prabhupant/python-ds/issues). It is also recommended to go through the Contributions Best Practices below to help organize contributions

## Contributions Best Practices

### Commits

* Write clear meaningful git commit messages (Do read [http://chris.beams.io/posts/git-commit/](http://chris.beams.io/posts/git-commit/))

* Make sure your PR's description contains GitHub's special numeric reference to the related issue.

* While adding questions, please make sure that you add only a single new question per PR as it becomes easy to review and maintain many PRs.

* When you make minor changes to a PR of yours, make sure you squash your commits afterwards so that you don't have an absurd number of commits for a single PR. (Learn how to squash commits at [https://davidwalsh.name/squash-commits-git](https://davidwalsh.name/squash-commits-git))

### Issues

Feel free to open up any issue in the repository, whether it is about code improvements or bug fixes or documentation. You can also use any label you want to associate with the issue. Please provide a clear description of the issue while filing it.

### Code Styling Guide

Python follows a Pep8 styling. Styling the code according to it makes it universally appealing and more readable. Also, if all data structures and algorithms are written in a similar style code, then it will be easy for everyone to implement them. So please follow Pep8 styling conventions (most notably, avoid using camelCase and prefer snake_case while naming functions and files). You can find the Pep8 styling guide here [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

### Questions

While there are infinite number of data structure and algorithm questions, it is impossible to collect all of them here. So please add only those questions that are either unique or tricky or have some mind blowing approach to solve them. Also, try not to file a PR for a question which is already present in the repo. Interesting questions and implementations are always welcomed.

For filing a PR for a new question, please open a issue first for the same and then reference it in the PR. For example, let's say you want to add a new question called "find max element in array". So first head over to the issues tab and create a new issue called "New question: find max element in array". Then if you want to work on it, please mention it in the description. After you are done writing the code and ready to file a PR, refer to the issue number in the PR description. Let's say the issue number was #23. So in the PR description, it should be "Fixes #23". That's it!

### Bookmarks

The Bookmarks directory is for storing awesome links to articles, videos, slides, talks, etc that are interesting and can help in increasing knowledge for a specific topic. There has been many PRs for adding new links in Bookmarks and most of them referred to either a whole book or DS Algo MOOCs, please refrain from adding them. Here are some points that you must consider before contributing to Bookmarks -

* Don't add a link to a MOOC or course (like DS Algo MIT lectures)

* Ask yourself "Is the link interesting enough that someone will really love it?" or "Is it something that an interviewer might ask in the interview to test you?" or "Is it some common or amazing thing people don't have enough knowledge about?". If yes to any of them, then sure, quickly file the PR.

* If an article has more than one part, be sure to refer to the first only in the PR.

## How To Contribute?

You can add anything to the repo as long as it is related to programming and increasing knowledge.

0. Firstly, fork the repo to your GitHub account. Just to get familiar with some terms, this will be the `origin`. To state `origin` and `upstream` explicitly,

https://github.com/prabhupant/python-ds = upstream
https://github.com/your-username/python-ds = origin

You will be making all your changes to origin and then file a PR to upstream from there.

1. Make sure to make a clone of the repository.

```bash
$ git clone https://github.com/prabhupant/python-ds
```

2. Now `cd` into the directory and create a new branch for the issue. Let's call the branch `max-number-in-array`

```bash
$ git checkout -b max-number-in-array
```

3. Make your changes and add and commit them

```bash
$ git add .
$ git commit -m "Add max number in array"
```

4. Now push the branch to your origin

```bash
$ git push origin max-number-in-array
```

5. Now head to your GitHub account and open your fork of python-ds i.e, the origin, and create a PR to the upstream from there. GitHub will automatically detect the upstream for you.

6. Write a good brief description and refer to the issue (if any) and submit the PR.

7. Now wait for the approval.

## Join The Development

Before you join the development, please fork and clone the repository to your local machine and explore it. Don't worry nothing will happen, atmost some code might not work :wink:

Feel free to contribute and be a part of this endeavour.



