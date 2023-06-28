'use client';
import React, { useEffect, useState } from 'react';
import { Button, Dropdown, Navbar, Avatar } from 'flowbite-react';
import Link from 'next/link';

// async function getCategorys() {
//   const response = await fetch("http://127.0.0.1:8000/categorys/", { cache: "no-store" });
//   const data = await response.json();
//   return data;
// }

export default function Header() {
  // const data = await getCategorys();
  // console.log(data);
  const [categorys, setCategorys] = useState([]);
  useEffect(() => {
    const fetchCategorys = async () => {
      const response = await fetch('http://127.0.0.1:8000/categorys/');
      const json = await response.json();
      setCategorys(json);
    };

    fetchCategorys();
  }, []);
  return (
    <Navbar
      fluid
      // rounded
      className='bg-blue-500'
    >
      <Navbar.Brand href="/">
        <img
          alt="Flowbite React Logo"
          className="mr-3 h-6 sm:h-9"
          src="/lion.jpg"
        />
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
          MyBlog
        </span>
      </Navbar.Brand>
      <div className="flex md:order-2">
        <Dropdown
          inline
          label={<Avatar alt="User settings" img="https://flowbite.com/docs/images/people/profile-picture-5.jpg" rounded/>}
        >
          <Dropdown.Header>
            <span className="block text-sm">
              Bonnie Green
            </span>
            <span className="block truncate text-sm font-medium">
              name@flowbite.com
            </span>
          </Dropdown.Header>
          <Dropdown.Item>
            Dashboard
          </Dropdown.Item>
          <Dropdown.Item>
            Settings
          </Dropdown.Item>
          <Dropdown.Item>
            Earnings
          </Dropdown.Item>
          <Dropdown.Divider />
          <Dropdown.Item>
            Sign out
          </Dropdown.Item>
        </Dropdown>
        <Navbar.Toggle />
      </div>
      <Navbar.Collapse>
        <Navbar.Link
          active
          href="#"
        >
          <p>
            Home
          </p>
        </Navbar.Link>
        <Navbar.Link href="#">
          About
        </Navbar.Link>
        <Navbar.Link href="#">
          Services
        </Navbar.Link>
        <Navbar.Link href="#">
          Pricing
        </Navbar.Link>
        <Navbar.Link href="#">
          Contact
        </Navbar.Link>
        <Dropdown
          inline
          label="Categories"
        >
          {categorys.map((category) => (
            <Link href={`/category/${category.slug}`}>
              <Dropdown.Item>
                <p>{category.title} (<small className='text-blue-400'>{category.posts.length}</small>)</p>
              </Dropdown.Item>
              </Link>
          ))}
        </Dropdown>
      </Navbar.Collapse>
    </Navbar>
  );
}

// export async function getStaticProps() {
//   const response = await fetch('http://127.0.0.1:8000/posts/')
//   const categorys = await response.json();

//   return {
//     props: {
//       categorys,
//     }
//   }
// }