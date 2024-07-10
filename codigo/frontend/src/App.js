import { RouterProvider } from "react-router-dom";
import AppRoutes from "./routes/router";

import "./styles/reset.css";
import "./styles/global.css";
/**
 * App Component
 * 
 * This component serves as the entry point for the application.
 * It wraps the application routes with the RouterProvider from react-router-dom, providing routing functionality.
 * Additionally, it applies global styles to reset and normalize CSS.
 * 
 * @returns {JSX.Element} App component.
 */
export default function App() {
    return <RouterProvider router={AppRoutes} />;
}
