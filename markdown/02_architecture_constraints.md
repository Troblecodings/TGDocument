# Architecture Constraints

The whole architecture of all our projects is generally constrained to cache
friendly and low overhead operations.

## Disallowed

Therefore, following things are not allowed.

| Disallowed                 | Description                                                                         | Example                                            |
| -------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------- |
| Exceptions                 | We don't want our game to crash midway. This adds a lot of unnecessary overhead (5) |                                                    |
| Cache unfriendly Container | A big risk to miss the L1 cache, which is the fastest cache (3)                     | `std::map, std::list, ...`                         |
| Per object function        | On a large scale those functions pile up a lot of overhead (5)                      | `texture.create();`                                |
| Object-Orientation         | The basic nature of object orientation misses the point of data transformation (5)  | `texture.getWidth(); // No optimization guarantee` |
| DLLs                       | They remove the the optimizers ability to optimize, which is really bad (2)         |                                                    |
| runtime polymorphism       | This hits cold memory and misses the branch prediction                                | `virtual toString();`                              |

## Reduced allowed

We try to reduce the usage of following things in performance critical systems.

| Reduced allowed                 | Description                                                                                                                                                                         | Example                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Template libraries              | While template libraries offer a great amount of flexibility and freedom, they also come at the cost of overhead, as the typesystem has to figure out the input type at runtime (4) | `glm::translate`                                              |
| Functions in structs or classes | This should only be used by entries on non-critical paths, as it possesses a big risk of potential overhead (4)(5)                                                                  | `struct _Test { const char* getTestName(); };`                |
| Global variables                | This adds startup overhead, so better not have too much (1)                                                                                                                         | `extern int x  = 0;`                                          |
| Copy and Swap                   | Try to avoid unnecessary copies and swaps                                                                                                                                           | `std::string name = "Test"; std::string name2 = name; //Copy` |
| High level abstraction          | Every abstraction comes with a cost, the lower the level the better (4)                                                                                                             | Code Generation, Classes, Templates                           |
| Smart pointer                   | They have hidden costs and threading issues (4)                                                                                                                                     | `std::unique_ptr<int>`                                        |

## Encouraged

In contrast to the list above, it is strongly recommended to use the following patterns and techniques.

| Encouraged                   | Description                                                                               | Example                        |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------ |
| Cache friendly containers    | Containers that barely miss L1 cache                                                      | `std::vector, std::array`      |
| `new` allocations            | Dynamic memory allocation (malloc)                                                        | `char* chars = new char[x]`    |
| low level abstractions       | This reduces abstraction cost                                                             | such as functions              |
| Structs                      | No need to worry about visibility                                                         | `struct T { int x; }`          |
| Namespaces                   | Every code should be within a namespace to reduce ambiguity                               | `namespace tge::test {}`       |
| Macros                       | Macros can shift some performance cost to compile time                                    | `#define CHECK(x) if(x) {}`    |
| `std::atomic`, `VkFence` ... | For thread safety                                                                         | `std::atomic<bool>`            |
| Fixed memory allocation      | Reduces the cost of dynamic allocation                                                    | `char test[25]`                |
| `inline`                     | Encourages the compiler to inline the function, to reduce calling overhead                | `inline void test() {}`        |
| `noexcept`                   | To be extra sure there are no exceptions                                                  | `void test() noexcept {}`      |
| Error return codes           | If there's the need for error handling                                                    | `if(vkCreateDevice(...))`      |
| Small size optimization      | Use pointers in dynamic lists and allocate the contents differently, when they are bigger | `std::vector<Test*>`           |
| `constexpr`, `consteval`     | This moves cost from the runtime to the compile time                                      | `constexpr uint32_t test = 32` |
| `const`                      | Gives the compiler a better base to optimize                                              | `void test(const char* name);` |
| GPU Memory                   | Everything should be copied to GPU memory as soon as possible                             |                                |
| `vector::reserve`            | Use `reserve` or `resize`, before using a vector to reduce the relocations                | `vec.reserve(200);`            |

## Additional

The systems need to run on different hardware whom themselves may have additional
hardware restrictions those should always we queried and cached while starting up.
Furthermore because of the Vulkan API, which the Engine and therefore a large part
of our systems are based on, enforces a lot of other restrictions, such as GPU
memory offsets, whom can also differ between hardware. Refer to
[The Vulkan Specification](https://www.khronos.org/registry/vulkan/specs/1.2-extensions/pdf/vkspec.pdf)
for more information. The project is currently required to use MSVC 2019 or newer as compiler. In release mode O2 optimization is being used. The software requires any sort of graphics module as hardware, which supports the vulkan api. This can either be a onboard graphics chip or a full on card. This also should run on all x86 and x64 processors.  

We also have a set of style guidelines for contributions to our repositories.
Refer to [troblecodings.com](https://troblecodings.com/contribution.html)

## Sources

(1) [CppCon 2018: Matt Godbolt “The Bits Between the Bits: How We Get to main"](https://www.youtube.com/watch?v=dOfucXtyEsU)

(2) [CppCon 2017: James McNellis “Everything You Ever Wanted to Know about DLLs”](https://www.youtube.com/watch?v=JPQWQfDhICA)

(3) [CppCon 2014: Chandler Carruth "Efficiency with Algorithms, Performance with Data Structures"](https://www.youtube.com/watch?v=fHNmRkzxHWs)

(4) [CppCon 2019: Chandler Carruth “There Are No Zero-cost Abstractions”](https://www.youtube.com/watch?v=rHIkrotSwcc)

(5) [CppCon 2014: Mike Acton "Data-Oriented Design and C++"](https://www.youtube.com/watch?v=rX0ItVEVjHc)
