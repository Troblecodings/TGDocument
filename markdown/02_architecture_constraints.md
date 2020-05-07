# Architecture Constraints

Generally the whole architecture of all our projects are constraint to cache friendly and low overhead operations.
Therefore following things are not allowed.
| Disallowed                 | Description                                                                           | Example                                                |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Exceptions                 | We don't want our game to crash midway. This adds a lot of unnecessary overhead (4)   |                                                        |
| Cache unfriendly Container | A big risk to miss the L1 cache               (3)                                 | ```std::map, std::list, ...```                         |
| Per object function        | On a large scale those functions pile up a lot of overhead     (4)                    | ```texture.create();```                                |
| Object-Orientation         | The basic nature of object orientation does miss the point of data transformation (4) | ```texture.getWidth(); // No optimization guarantee``` |
| DLLs                       | They remove the the optimizers ability to optimize, which is really bad  (2)          |                                                        |

We try to reduce the usage of certain things in performance critical systems

| Reduced allowed                 | Description                                                                                                                                                                           | Example                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Template libraries              | While template libraries offer a great amount of flexibility and freedom they also come at the cost of overhead as the typesystem has to figure out the input type at the runtime (4) | ```glm::translate       ```                                       |
| Functions in structs or classes | This should only be used by entries on none critical paths as it possess a big risk of potential overhead (4)(5)                                                                      | ```struct _Test { const char* getTestName(); };```                |
| Global variables                | This adds startup overhead, so better not have to much (1)                                                                                                                            | ```extern int x  = 0;```                                          |
| Copy and Swap                   | Try to avoid unnecessary copies and swaps                                                                                                                                             | ```std::string name = "Test"; std::string name2 = name; //Copy``` |
| High level abstraction          | Every abstraction comes with a cost, the lower the level the better (4)                                                                                                               | Code generation, Classes, Templates                               |

(1) [CppCon 2018: Matt Godbolt “The Bits Between the Bits: How We Get to main"](https://www.youtube.com/watch?v=dOfucXtyEsU)

(2) [CppCon 2017: James McNellis “Everything You Ever Wanted to Know about DLLs”](https://www.youtube.com/watch?v=JPQWQfDhICA)

(3) [CppCon 2014: Chandler Carruth "Efficiency with Algorithms, Performance with Data Structures"](https://www.youtube.com/watch?v=fHNmRkzxHWs)

(4) [CppCon 2019: Chandler Carruth “There Are No Zero-cost Abstractions”](https://www.youtube.com/watch?v=rHIkrotSwcc)

(5) [CppCon 2014: Mike Acton "Data-Oriented Design and C++"](https://www.youtube.com/watch?v=rX0ItVEVjHc)