import { Link } from "react-router-dom";

const Header = () => {
  return (
    <div className="flex justify-between shadow-lg m-2 bg-green-100 rounded-lg sm:bg-yellow-100 lg:bg-pink-100">
      <div>
        <img
          className="w-36 mix-blend-multiply"
          src="https://img.freepik.com/premium-vector/helmet-vector-helmet-illustration-helmet-logo-design-bike-helmet_921448-846.jpg?w=740"
        ></img>
      </div>
      <div className="flex items-center">
        <ul className="flex p-4 m-4">
          <li className="px-6">
            <Link to={"/"}>Home</Link>
          </li>
          <li className="px-6">
            <Link to={"/about"}>About Us</Link>
          </li>
          <li className="px-6">
            <Link to={"/contact"}>Contact Us</Link>
          </li>
          <li className="px-6">
          <Link to={"/"}>Login</Link>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Header;
