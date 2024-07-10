import { createBrowserRouter } from "react-router-dom";

import InitialPage from "../pages/InitialPage";
import HomePage from "../pages/HomePage";
import RoutesPage from "../pages/RoutesPage";
import ComparisonPage from "../pages/ComparisonPage";
/**
 * AppRoutes Component
 * 
 * This component configures the routes for the application using react-router-dom's createBrowserRouter function.
 * It defines the paths and their corresponding components for routing within the application.
 * 
 * @returns {JSX.Element} AppRoutes component.
 */
const AppRoutes = createBrowserRouter([
    {
        path: "/",
        element: <InitialPage />,
    },
    {
        path: "/home",
        element: <HomePage />,
    },
    {
        path: "/routes",
        element: <RoutesPage />,
    },
    {
        path: "/comparison",
        element: <ComparisonPage />,
    },
]);

export default AppRoutes;
