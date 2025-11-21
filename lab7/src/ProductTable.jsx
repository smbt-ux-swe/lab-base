import ProductRow from "./ProductRow";

function ProductTable({ products, onToggleFavorite }) {
  console.log("ProductTable render");

  return (
    <table border="1" cellPadding="8">
      <thead>
        <tr>
          <th>Name</th>
          <th>Category</th>
          <th>Price</th>
          <th>Fav</th>
        </tr>
      </thead>

      <tbody>
        {products.map((product) => (
          <ProductRow
            key={product.id}
            product={product}
            onToggleFavorite={onToggleFavorite}
          />
        ))}
      </tbody>
    </table>
  );
}

export default ProductTable;
