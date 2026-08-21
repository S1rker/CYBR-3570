# CYBR 3570: Cryptography
## Fall 2026

 
### Course Description
Cryptography is the foundation of modern cybersecurity. Nearly every secure technology—from online banking and messaging applications to virtual private networks, password managers, cloud storage, and software updates—depends on cryptographic techniques. Understanding how these techniques work, why they are secure, and how they should be applied is an essential skill for cybersecurity professionals.
This course provides a practical introduction to modern cryptography and cryptanalysis. Students will explore the historical development of cryptography, the mathematical foundations that support modern cryptographic systems, and the algorithms and protocols used to secure today's information systems. Emphasis is placed on understanding how cryptography is correctly integrated into real-world software rather than developing new cryptographic algorithms.
Throughout the semester, students will build a reusable Python-based cryptographic toolkit that demonstrates both classical and modern cryptographic concepts.
 
### Course Learning Outcomes
Upon successful completion of this course, students should be able to:
- Explain the purpose and limitations of cryptography.
- Differentiate between confidentiality, integrity, authentication, and non-repudiation.
- Explain both classical and modern cryptographic algorithms.
- Apply modular arithmetic and related mathematical concepts used in cryptography.
- Analyze the strengths and weaknesses of cryptographic systems.
- Explain the operation of symmetric and public-key cryptography.
- Understand the purpose and operation of hash functions, message authentication codes, and digital signatures.
- Describe the operation of Public Key Infrastructure (PKI) and certificate-based authentication.
- Identify common cryptographic implementation mistakes and security failures.
- Correctly implement cryptographic solutions using established Python libraries.
 
### Course Philosophy
This course emphasizes applied cryptography rather than theoretical cryptography.
Students are not expected to become cryptographers or develop new encryption algorithms.
Instead, students will learn to:
- understand cryptographic systems,
- evaluate cryptographic designs,
- recognize insecure implementations,
- correctly use modern cryptographic libraries, and
- integrate cryptography into secure software systems.
A recurring theme throughout the semester is:
**Never roll your own cryptography.**
Students will learn why modern cryptographic libraries exist and how to use them appropriately.
 
### Required Textbook
#### Primary Text
Jean-Philippe Aumasson
Serious Cryptography (Second Edition)
No Starch Press
https://learning.oreilly.com/library/view/serious-cryptography-2nd/9781098182472/

 
#### Supplemental Text
Christof Paar and Jan Pelzl
Understanding Cryptography: A Textbook for Students and Practitioners

Selected sections will be assigned throughout the semester to supplement mathematical concepts and provide additional examples.
 
#### Software Requirements
Students will use the following software throughout the semester:
- Python 3.12+
- JupyterLab
- Git
- Visual Studio Code (recommended)
- PyCryptodome
- cryptography
- pytest
- matplotlib
- numpy
Installation instructions will be provided during the first week of class.
 
### Course Structure
Most weeks follow a common pattern.
Monday
- New concepts
- Lecture
- Discussion
- Demonstrations
Wednesday
- Algorithms
- Mathematics
- Live coding
- Begin weekly laboratory notebook
Students complete:
- Reading assignment
- Weekly notebook
- Toolkit updates
- Quiz (when assigned)
 
### The Cryptographic Toolkit
Rather than completing isolated programming assignments, students will spend the semester developing a reusable Python package called the Cryptographic Toolkit.
Each week introduces additional capabilities, including:
- Classical ciphers
- Modular arithmetic
- Random number generation
- Symmetric encryption
- Hash functions
- Public-key cryptography
- Digital signatures
- Secure protocols
By the end of the semester, students will possess a complete educational cryptography library that serves as the foundation for the semester project.
 
### Weekly Crypto Labs
Each laboratory is completed using Jupyter Notebooks.
Labs include:
- Reading questions
- Conceptual questions
- Mathematical exercises
- Python programming
- Security engineering discussions
- Reflection questions
The purpose of these assignments is to reinforce lecture concepts through hands-on exploration rather than memorization.
 
### Semester Project
Students will complete an individual programming project that demonstrates the correct use of modern cryptographic techniques.
Possible projects include:
- Secure file encryption utility
- Password manager
- Digital signature application
- Certificate explorer
- Secure notes application
- Encrypted messaging prototype
- Educational TLS demonstration
The project includes:
- Proposal
- Progress review
- Final implementation
- Demonstration
- Technical report
 
### Grading
| Category | Weight |
| ----- | ----- |
| Weekly Crypto Labs | 35% |
| Reading Quizzes | 10% | 
| Midterm Examination | 15% |
| Final Examination	| 20% |
| Semester Project | 15% |
| Participation / Professionalism | 5% |
 
#### Grading Scale
| Percentage | Grade |
| ----- | ----- |
| 93–100 | A |
| 90–92	| A- |
| 87–89	| B+ |
| 83–86	| B |
| 80–82	| B- |
| 77–79	| C+ |
| 73–76	| C |
| 70–72	| C- |
| 67–69	| D+ |
| 63–66	| D |
| 60–62	| D- |
| Below 60 | F |
 
### Attendance
Students are expected to attend class and actively participate in discussions and laboratory activities.
Many classroom demonstrations and cryptographic exercises are difficult to replicate outside of class.
Attendance alone does not guarantee success, but active participation is strongly correlated with improved performance.
 
### Late Work
Weekly laboratories are designed to prepare students for future material and should be completed on time.
Late submissions may receive reduced credit unless prior arrangements have been made or university-approved circumstances apply.
Specific policies and deadlines will be communicated through Canvas.
 
### Examinations
Both the midterm and final examinations are open-book and open-note.
Examinations emphasize:
- conceptual understanding,
- mathematical reasoning,
- code interpretation,
- security analysis, and
- practical application.
Students should expect to explain design decisions rather than memorize algorithm details.
 
### Artificial Intelligence Policy
Artificial intelligence tools are becoming a normal part of modern software development and cybersecurity practice. Their use is permitted within the following expectations.
Students may use AI tools to:
- explain concepts,
- assist with debugging,
- explore alternative implementations,
- improve documentation,
- review Python syntax.
Students are responsible for understanding every line of code they submit.
Any submitted work must accurately represent the student's own understanding. Students who cannot explain code or written responses included in their submissions may receive reduced credit or be referred for academic integrity review.
The goal of this course is not simply to produce working code, it is to develop the ability to evaluate and correctly apply cryptographic techniques.
 
### Academic Integrity
Students are expected to uphold the highest standards of academic honesty.
Unless explicitly stated otherwise, all submitted work must be completed individually.
Copying code, sharing solutions, or submitting work generated entirely by another individual or automated system without understanding or attribution constitutes academic misconduct.
University policies regarding academic integrity apply to all assignments and examinations.
 
### Communication
Canvas will serve as the official course management system.
Students are responsible for regularly checking:
- Announcements
- Assignment updates
- Due dates
- Grades
Email should be used for questions requiring personal responses.
 
### Tentative Course Schedule
| Week | Topics |
| ----- | ----- |
| 1	| Introduction to Cryptography, Security Goals, Classical Cryptography |
| 2	| Mathematical Foundations |
| 3	| Randomness and Entropy |
| 4	| Symmetric Cryptography |
| 5	| AES |
| 6 | Modes of Operation |
| 7	| Hash Functions |
| 8	| Message Authentication |
| 9	| Midterm Examination / PKI |
| 10 | Public-Key Mathematics |
| 11 | RSA |
| 12 | Diffie–Hellman and Elliptic Curves |
| 13 | Digital Signatures |
| 14 | TLS, Certificates, Secure Protocols |
| 15 | Cryptographic Failures, Quantum Computing, Review |
| 16| Final Examination / Project Submission |
 
### Course Themes
Throughout the semester, students should continually ask:
- Why does it work?
- What assumptions make it secure?
- How can it fail?
- Where is it used in modern systems?
Understanding these questions is considerably more valuable than memorizing algorithms.



