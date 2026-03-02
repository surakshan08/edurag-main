export default function SourceBadge({ category }) {
  return (
    <span className="px-3 py-1 text-xs rounded-full bg-slate-700 text-slate-200">
      {category.replace("_", " ")}
    </span>
  );
}
