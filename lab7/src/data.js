export const products = Array.from({ length: 100 }, (_, idx) => {
    const categories = ["book", "device", "etc"];
    return {
      id: idx + 1,
      name: `Product ${idx + 1}`,
      category: categories[idx % 3],
      price: Math.floor(Math.random() * 100) + 1,
      favorite: false,
    };
  });
  