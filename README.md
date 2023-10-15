# IAS-Project

Information Assurance and Security Project 6th semester

The widespread adoption of Android devices and their capability to access significant private and confidential information have resulted in these devices being targeted by malware developers. Existing Android malware analysis techniques can be broadly categorized into static and dynamic analysis. In this paper, we present two machine learning aided approaches for static analysis of Android malware. The first approach is based on permissions and the other is based on source code analysis utilizing a bag-of-words representation model. Our permission-based model is computationally inexpensive, and is implemented as the feature of OWASP Seraphimdroid Android app that can be obtained from Google Play Store. Our evaluations of both approaches indicate an F-score of 95.1% and F-measure of 89% for the source code-based classification and permission-based classification models, respectively.

We presented two machine learning aided (classification and clustering) approaches based on app permissions and
source code analysis to detect and analyze malicious Android apps. The use of machine learning allows our algorithms
to detect new malware families with high precision and recall rates. Our approach complements existing signature-based
anti-malware solutions, as the latter is not capable of detecting malicious software until the appropriate signatures are released. Specifically, we demonstrated that the permission-based method was able to classify malware from goodware in 89%
of cases while source code analysis classification performance was over 95%. Accuracy rates of 95.1% using SVM, and 95.6%
using the ensemble learning method are comparable with existing state-of-the art solutions.
