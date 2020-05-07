# Architecture Constraints

Generally the whole architecture of all our projects are constraint to cache friendly and low overhead operations.

## Disallowed
Therefore following things are not allowed.

| Disallowed                 | Description                                                                           | Example                                                |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Exceptions                 | We don't want our game to crash midway. This adds a lot of unnecessary overhead (5)   |                                                        |
| Cache unfriendly Container | A big risk to miss the L1 cache               (3)                                     | ```std::map, std::list, ...```                         |
| Per object function        | On a large scale those functions pile up a lot of overhead     (5)                    | ```texture.create();```                                |
| Object-Orientation         | The basic nature of object orientation does miss the point of data transformation (5) | ```texture.getWidth(); // No optimization guarantee``` |
| DLLs                       | They remove the the optimizers ability to optimize, which is really bad  (2)          |                                                        |
| runtime polymorphism       | This will hit cold memory and miss the branch prediction                              | ```virtual toString();```                              |

## Reduced allowed

We try to reduce the usage of certain things in performance critical systems

| Reduced allowed                 | Description                                                                                                                                                                           | Example                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Template libraries              | While template libraries offer a great amount of flexibility and freedom they also come at the cost of overhead as the typesystem has to figure out the input type at the runtime (4) | ```glm::translate       ```                                       |
| Functions in structs or classes | This should only be used by entries on none critical paths as it possess a big risk of potential overhead (4)(5)                                                                      | ```struct _Test { const char* getTestName(); };```                |
| Global variables                | This adds startup overhead, so better not have to much (1)                                                                                                                            | ```extern int x  = 0;```                                          |
| Copy and Swap                   | Try to avoid unnecessary copies and swaps                                                                                                                                             | ```std::string name = "Test"; std::string name2 = name; //Copy``` |
| High level abstraction          | Every abstraction comes with a cost, the lower the level the better (4)                                                                                                               | Code generation, Classes, Templates                               |
| Smart pointer                   | Those have hidden costs and threading issues (4)                                                                                                                                      | ```std::unique_ptr<int>```                                        |

## Encouraged

In contrast to the lists above it is strongly recommended to use the following patterns and technics.

| Encouraged               | Description                                                                            | Example                            |
| ------------------------ | -------------------------------------------------------------------------------------- | ---------------------------------- |
| cache friendly Container | Container that barely miss L1 cache                                                    | ```std::vector, std::array```      |
| `new` allocations        | This allocates memory dynamically (malloc)                                             | ```char* chars = new char[x]```    |
| low level abstractions   | This reduces abstraction cost                                                          | such as functions                  |
| structs                  | No need to worry about visibility                                                      | ```struct T { int x; }```          |
| namespaces               | Every code should be within a namespace to reduce ambiguity                            | ```namespace tge::test {}```       |
| Macros                   | Macros can shift some performance cost to the compile time                             | ```#define CHECK(x) if(x) {}```    |
| std::atomic, VkFence ... | for thread safety                                                                      | ```std::atomic<bool>```            |
| fixed memory allocation  | reduces the cost of dynamic allocation                                                 | ```char test[25]```                |
| `inline`                 | Encourages the compile to inline the function to reduce calling overhead               | ```inline void test() {}```        |
| `noexcept`               | To be extra sure there are no exceptions                                               | ```void test() noexcept {}```      |
| Error return codes       | If there should be the need for error handling                                         | ```if(vkCreateDevice(...))```      |
| Small size optimization  | use pointers in dynamic lists and allocate the contents differently if they are bigger | ```std::vector<Test*>```           |
| constexpr, consteval     | this moves cost from the runtime to the compile time                                   | ```constexpr uint32_t test = 32``` |
| const                    | Gives the compile a better base to optimize                                            | ```void test(const char* name);``` |
| GPU Memory               | Everything should be copied to GPU memory as soon as possible                          |                                    |

## Additional

The systems need to run on different hardware whom themselves may have additional hardware restrictions those should always we queried and cached while starting up. Furthermore because of the Vulkan API, which the Engine and therefore a large part of our systems is based on, enforces a lot of other restrictions, such as GPU memory offsets, whom can also differ between hardware. For more information on the Vulkan restrictions visit [The Vulkan Specification](https://www.khronos.org/registry/vulkan/specs/1.2-extensions/pdf/vkspec.pdf)

We also have a set of style guidelines for contributions to our repositories. To see them visit [troblecodings.com](https://troblecodings.com/contribution.html)

## Sources

(1) [CppCon 2018: Matt Godbolt “The Bits Between the Bits: How We Get to main"](https://www.youtube.com/watch?v=dOfucXtyEsU)

(2) [CppCon 2017: James McNellis “Everything You Ever Wanted to Know about DLLs”](https://www.youtube.com/watch?v=JPQWQfDhICA)

(3) [CppCon 2014: Chandler Carruth "Efficiency with Algorithms, Performance with Data Structures"](https://www.youtube.com/watch?v=fHNmRkzxHWs)

(4) [CppCon 2019: Chandler Carruth “There Are No Zero-cost Abstractions”](https://www.youtube.com/watch?v=rHIkrotSwcc)

(5) [CppCon 2014: Mike Acton "Data-Oriented Design and C++"](https://www.youtube.com/watch?v=rX0ItVEVjHc)