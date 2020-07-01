# Solution Strategy

Most of our decision making comes down to performance and future-proofing. We
can attain performance by disregarding an object-oriented structure and focusing
on a data-oriented one instead, which can be seen by the exclusion of classes to
the project and uses of structs in its place. Other things to consider while
developing the engine are using/managing memory efficiently with consideration
of the L1 cache, which is the fastest of all available caches. This is
accomplished by constraining use of more complex data types and using
cache-friendlier data types instead. One example would be to use `std::vector`
instead of `std::list`. Similar thinking is applied to other fields as well.
